from context import unittest, os, DiscriminatorGenerator

top = os.getcwd()

class TestGeneratorPretrainingGenerator(unittest.TestCase):
    def sub_test(self, actual, expected, msg=None):
        with self.subTest(actual=actual, expected=expected):
            self.assertEqual(actual, expected, msg=msg)

    def test_generator_pretraining_generator(self):
        gen = DiscriminatorGenerator(
            path_pos=os.path.join(top, 'data', 'prideandprejudice.txt'),
            path_neg=os.path.join(top, 'tests', 'data', 'sample_generated.txt'),
            B=1,
            shuffle=False)
        gen.reset()
        x, y = gen.next()
        expected_text = ['PRIDE', 'AND', 'PREJUDICE', '</S>']
        length = len(expected_text)
        actual_text = [gen.id2word[id] for id in x[0][:length]]
        self.sub_test(actual_text, expected_text, msg='x text test')
        self.sub_test(y[0], 1, msg='true data')


        x, y = gen.__getitem__(idx=gen.n_data_pos-1)
        expected_text = ['sensible', 'of', 'the', 'warmest', 'gratitude',
                         'towards', 'the', 'persons', 'who,', 'by', 'bringing',
                         '</S>'
                        ]
        expected_ids = [gen.word2id[word] for word in expected_text]
        actual_ids = x[0][:len(expected_ids)]
        result = (actual_ids == expected_ids).all()
        self.assertTrue(result, msg='x ids test')
        self.sub_test(y[0], 0, 'generated data')
