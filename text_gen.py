import os
import random

# Directory containing the audio files C:\Users\Marouane\workflow\S8\vsep\Input\test\out-5\wsj0-new
audio_dir = "C:/Users/Marouane/workflow/S8/vsep/Input/"

# List of speakers (folder names)
speakers = os.listdir(audio_dir)
print(speakers)
# Map each file to the number of pairs it appears in

file_counts = {f: 0 for c in speakers  for f in os.listdir(os.path.join(audio_dir, c))}
print(file_counts)

# Pair up files with different speakers and give them opposite SNR scores
pairs = []
for i, s1 in enumerate(speakers):
    for j, s2 in enumerate(speakers):
        if i != j:
            # Find all files for each speaker
            files1 = [f for f in os.listdir(os.path.join(audio_dir, s1))]
            files2 = [f for f in os.listdir(os.path.join(audio_dir, s2))]
            # Pair up files randomly and give them opposite SNR scores
            for f1 in files1:
                for f2 in files2:
                    if file_counts[f1] < 1 and file_counts[f2] < 1:
                        snr = random.uniform(0.5, 2)  # Generate random SNR
                        pairs.append((f"{audio_dir[46:51]}/{s1}/{f1}", snr, f"{audio_dir[46:51]}/{s2}/{f2}", -snr))
                        file_counts[f1] += 1
                        file_counts[f2] += 1

# Write pairs to file
with open("pairs.txt", "w") as f:
    for p in pairs:
        f.write(f"{p[0]} {p[1]} {p[2]} {p[3]}\n")

# Read file pairs and SNR scores
with open('pairs.txt', 'r') as f:
    file_pairs = [line.strip().split() for line in f]

# Shuffle file pairs
random.shuffle(file_pairs)

# Split into train, test, and cross-validation sets
n_pairs = len(file_pairs)
n_train = int(0.7 * n_pairs)
n_test = int(0.1 * n_pairs)
n_cv = n_pairs - n_train - n_test

train_pairs = file_pairs[:n_train]
test_pairs = file_pairs[n_train:n_train+n_test]
cv_pairs = file_pairs[n_train+n_test:]

# Write to text files
with open('mix_2_spk_tr.txt', 'w') as f:
    f.write('\n'.join([' '.join(pair) for pair in train_pairs]))

with open('mix_2_spk_tt.txt', 'w') as f:
    f.write('\n'.join([' '.join(pair) for pair in test_pairs]))

with open('mix_2_spk_cv.txt', 'w') as f:
    f.write('\n'.join([' '.join(pair) for pair in cv_pairs]))
