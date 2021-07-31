import json

class Fingerprint:
    def loadFinger(path):
        try:
            finger_file =  open(path, 'r')
            finger_content = json.loads(finger_file.read())
            def_sha = finger_content['sha']
            return def_sha
        except Exception as e:
            print(f"Could not load fingerprint: {e}")

    def loadFinger_full(path):
        try:
            finger_file =  open(path, 'r')
            finger_content = json.loads(finger_file.read())
            return json.dumps(finger_content)
        except Exception as e:
            print(f"Could not load fingerprint: {e}")