# AGROSmart — Leaf Disease Detection (PlantVillage)

AGROSmart is a lightweight computer vision pipeline for **plant leaf health classification**. It uses a Convolutional Neural Network (CNN) to classify images as **healthy** or **diseased**, then exports prediction results to structured files for analysis.

## Features
- Loads the PlantVillage dataset from disk
- Converts multi-class labels into a binary problem (healthy vs diseased)
- Applies data augmentation and normalization
- Trains a CNN using TensorFlow/Keras
- Evaluates model performance using accuracy, confusion matrix and classification report
- Exports predictions to **CSV** and **JSON** for downstream analysis

## Project Structure
- `main.ipynb` — Notebook with the full training + evaluation pipeline (no markdown cells; all logic is in code with comments)
- `documentation.md` — Technical documentation with detailed explanations of the pipeline
- `dataset/PlantVillage` — Expected location for the downloaded PlantVillage dataset

## Usage
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd agro_computer_vision
   ```

2. Install dependencies (recommend using a virtual environment):
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS/Linux
   .\.venv\Scripts\activate   # Windows

   pip install -r requirements.txt
   ```

3. Place the PlantVillage dataset under `dataset/PlantVillage`.
   The folder should contain subfolders for each class (e.g., `Tomato_healthy`, `Tomato_Early_blight`, etc.).

4. Run the notebook:
   - Open `main.ipynb` in Jupyter or VS Code and execute cells sequentially.

## Output
The notebook generates:
- `leaf_classification_results.csv` — predictions per image (`true_label`, `predicted_label`, `confidence`)
- `leaf_classification_results.json` — the same results in JSON

## Requirements
- Python 3.8+
- TensorFlow
- NumPy
- pandas
- matplotlib
- scikit-learn

## Notes
- This project is a prototype: for production use, consider adding model checkpointing, better train/val split, and a more robust dataset handling pipeline.
- For real-world deployment, combine with a capture pipeline (mobile app, drone, camera), and store results in a database.

---

If you want, I can also add instructions to run the model on new image files (outside the PlantVillage dataset), or include a pre-trained model export step.