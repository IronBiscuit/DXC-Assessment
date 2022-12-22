import argparse
import sys

from CharacterLoader import CharacterLoader
from Decoder import *
from Encoder import *



if __name__ == "__main__":
    cl = CharacterLoader("characters.txt")
    ic_dict, ci_dict = cl.get_ref_dicts()

    encoder = Encoder(ci_dict, ic_dict)
    decoder = Decoder(ci_dict, ic_dict)

    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--command', help='Type of command', required=True)
    parser.add_argument('-t','--text', help='The text argument', required=True)
    parser.add_argument('-o','--offset', help='The offset character', required=True)
    
    args = vars(parser.parse_args())

    cmd_type = args['command'].lower()

    if (cmd_type != "encode" and cmd_type != "decode"):
        print("Invalid command type, please try again!")
        sys.exit()
    
    try:
        if (cmd_type == "encode"):
            result = encoder.encode(args['text'], args['offset'])
            print(result)
        else:
            result = decoder.decode(args['text'], args['offset'])
            print(result)

    except EncodeException as e:
        print("Error in encoding: " + str(e))
        sys.exit()
    
    except DecodeException as e:
        print("Error in decoding: " + str(e))
        sys.exit()


