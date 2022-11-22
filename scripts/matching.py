import time
import sys
import time
from argparse import ArgumentParser
from deepface import DeepFace
import numpy as np

def matching(img1, img2):
    #match
    result = DeepFace.verify(img1_path = img1, img2_path = img2)
    # return True or False
    sim = str(result.get("verified"))
    return sim

    # keep the shell open so we can debug

# execution order matters -this puppy has to be at the bottom as our functions are defined above
if __name__ == '__main__':
    parser = ArgumentParser(description='A simple argument input example')
    parser.add_argument("-img1", "--input", dest="in1", help="img1", required=True)
    parser.add_argument("-img2", "--input2", dest="in2", help="img2", required=True)    
    args = parser.parse_args()
    t = vars(args)
    #Extract images
    img1 = t.get("in1")
    img2 = t.get("in2")
    match =matching(img1, img2)
    #Write output
    sys.stdout.write(match)