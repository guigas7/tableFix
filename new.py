from chardet.universaldetector import UniversalDetector

def test_encoding(file_name):
    detector = UniversalDetector()
    print('starting to feed the detector')
    with open(file_name, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                 break
        detector.close()
    print('finished that')
    r = detector.result
    return "Detected encoding %s with confidence %s" % (r['encoding'], r['confidence'])

print(test_encoding('input.csv'))