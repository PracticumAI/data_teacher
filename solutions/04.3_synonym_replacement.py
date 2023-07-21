from textaugment import EDA
eda_augment = EDA()
TEST_TEXT = "The sun is shining brightly in the clear blue sky."
syn_augmented = eda_augment.synonym_replacement(TEST_TEXT)
print("ORIGINAL Text :",TEST_TEXT)
print("AUGMENTED TEXT:", syn_augmented)