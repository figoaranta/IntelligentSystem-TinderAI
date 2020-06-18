from classifier import Classifier
import person_detector
import tensorflow as tf
from time import time
import wrapper

if __name__ == "__main__":
    token = "432358fb-0ec5-4233-8660-1bdd8235c039"
    api = wrapper.tinderAPI(token)

    # Coco mobilenet graph
    detection_graph = person_detector.open_graph()
    with detection_graph.as_default():
        with tf.Session() as sess:

            classifier = Classifier(graph="./tf/training_output/retrained_graph.pb",
                                    labels="./tf/training_output/retrained_labels.txt")

            end_time = time() + 60*60*2
            x = 0
            while time() < end_time:
                pos_schools = ["Binus University", "Binus University Internatinal"]
                try:
                    persons = api.nearby_persons()
                    for peep in persons:
                        print("Stage 1 : Success")
                        score = peep.predict_likeliness(classifier, sess)
                        print("Stage 2 : Success")
                        print("-------------------------")
                        print("ID: ", peep.id)
                        print("Name: ", peep.name)
                        print("Schools: ", peep.schools)
                        print("Images: ", peep.images)
                        print(score)

                        if score > 0.8:
                            res = peep.like()
                            print("LIKE")
                        else:
                            res = peep.dislike()
                            print("DISLIKE")
                        print("Stage 3 : Success")
                except Exception:
                    pass

    classifier.close()