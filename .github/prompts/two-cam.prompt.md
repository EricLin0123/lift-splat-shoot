Now I have a custom image data set with only two camera perspectives, one front and one back. The dataset is structured like below:
custom-data
├── front
| ├──1.png
| ├──2.png
| ├──...
├── back
| ├──1.png
| ├──2.png
| ├──...

These images do not have any metadata nor annotations. The file name implies the timestamp, i.e., 1.png is the first frame, 2.png is the second frame, and so on.

I want you to help me modify the code so that I can use this custom dataset to run inference and visualize the model predictions.

note that the original code is designed to work with a dataset that has multiple camera perspectives and includes metadata and annotations. Since my custom dataset only has two camera perspectives and lacks metadata, I need to adjust the code accordingly.

Notice that there is a version parameter in the code, which indicates different dataset configurations. I want to set version=custom to indicate that I am using my custom dataset.
