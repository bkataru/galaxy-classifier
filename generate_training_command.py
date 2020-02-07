import os

cmd_list = [
    'python',
    '{}\\retrain.py'.format(os.getcwd()),
    '--bottleneck_dir={}\\bottlenecks'.format(os.getcwd()),
    '--how_many_training_steps 500',
    '--model_dir={}\\inception'.format(os.getcwd()),
    '--output_graph={}\\retrained_graph.pb'.format(os.getcwd()),
    '--output_labels={}\\retrained_labels.txt'.format(os.getcwd()),
    '--image_dir {}\\tf_files'.format(os.getcwd())
]

cmd = ' '.join(cmd_list)
print("Your command: ")
print(cmd)