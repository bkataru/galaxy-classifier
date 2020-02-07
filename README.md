# Galaxy Image Classifier

A CNN to classify images different types of galaxies - spiral, elliptical, and irregular. 

Trained and tested on 16 gigs of RAM, i7-8750H, GTX 1060 all at stock settings.

Check `requirements.txt` and `packages_neded.txt` for module information.

## Quick start

### To train: 
- First generate the training command using `generate_training_command.py`
  ```shell
  python generate_training_command.py
  ```
- Then execute the command which will be of this form:
  ```shell
  python your_project_path\retrain.py --bottleneck_dir=your_project_path\bottlenecks --how_many_training_steps 500 --model_dir=your_project_path\inception --output_graph=your_project_path\retrained_graph.pb --output_labels=your_project_path\retrained_labels.txt --image_dir your_project_path\tf_files
  ```
  You can change the number of training steps and other parameters inside the `generate_training_command.py` file. 
### To predict 
```zh
python label_image.py test_images/ellipticaltest.jpg
```
Output:
```shell
elliptical (score = 98.54690)
spiral (score = 0.86201)
irregular (score = 0.59109)
```
