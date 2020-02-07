import os

directory = os.getcwd()

cmd_list = [
    'python',
    '{}\\retrain.py'.format(directory),
    '--bottleneck_dir={}\\bottlenecks'.format(directory),
    '--how_many_training_steps 500',
    '--model_dir={}\\inception'.format(directory),
    '--output_graph={}\\retrained_graph.pb'.format(directory),
    '--output_labels={}\\retrained_labels.txt'.format(directory),
    '--image_dir {}\\tf_files'.format(directory)
]

cmd = ' '.join(cmd_list)
print("Your command: ")
print(cmd)