import os
import person_detector
import tensorflow as tf

IMAGE_FOLDER = "./images/unclassified"
POS_FOLDER = "./images/classified/positive"
NEG_FOLDER = "./images/classified/negative"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == "__main__":
    detection_graph = person_detector.open_graph()

    images = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]
    positive_images = filter(lambda image: (image.startswith("1_")), images)
    negative_images = filter(lambda image: (image.startswith("0_")), images)

    with detection_graph.as_default():
        with tf.Session() as sess:


            for neg in negative_images:
                old_filename = IMAGE_FOLDER + "/" + neg
                new_filename = NEG_FOLDER + "/" + neg[:-5] + ".jpg"
                if not os.path.isfile(new_filename):
                    try:
                        img = person_detector.get_person(old_filename, sess)
                        if not img:
                            continue
                        img = img.convert('L')
                        img.save(new_filename, "jpeg")
                    except Exception as e:
                        continue
                        
            for pos in positive_images:
                old_filename = IMAGE_FOLDER + "/" + pos
                new_filename = POS_FOLDER + "/" + pos[:-5] + ".jpg"
                if not os.path.isfile(new_filename):
                    img = person_detector.get_person(old_filename, sess)
                    if not img:
                        continue
                    img = img.convert('L')
                    img.save(new_filename, "jpeg")