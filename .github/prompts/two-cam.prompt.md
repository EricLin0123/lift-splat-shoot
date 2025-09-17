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

These images do not have any metadata nor annotations. The file name implies the timestamp, i.e., 1.png is the first frame, 2.png is the second frame, and so on. I want you to help me modify the code so that I can use this custom dataset to run inference and visualize the model predictions.

Answer:
How to run

Put your custom dataset under, for example: /data/custom-data with subfolders front/ and back/.
Run: python main.py viz_model_preds --dataset=custom --dataroot=/data/custom-data --modelf=/path/to/model.pt --output_folder=./out --cams='["front","back"]' --bsz=1
Notes:
Intrinsics/extrinsics are fabricated; predictions are for visualization only.
