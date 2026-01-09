# Emotion Detection using Deep Neural Networks
This project implements an end-to-end Emotion Detection system using Deep Neural Networks in PyTorch. 
The model classifies human emotions from text by learning contextual patterns using an LSTM-based architecture.

## Problem Statement 
Understanding human emotions from text is an important task in Natural Language Processing (NLP).This project aims to build a Deep Learning model that can automatically classify emotions from textual data,which can be useful in applications such as chatbots, customer feedback analysis, and mental health monitoring.



## Dataset Description
The project uses a real-world multi-class emotion dataset consisting of text samples labeled with emotion classes.
The dataset is split into:
- Training set (training.csv)
- Validation set (validation.csv)
- Test set (test.csv)

Each file contains:
- text: Input sentence
- label: Emotion class (0–5)

## Model Architecture

The Emotion Detection model is based on a Deep Neural Network with the following architecture:

Input Text
- Tokenization & Padding
- Embedding Layer
- LSTM Layer
- Fully Connected Layer
- Emotion Class Prediction

## Technologies & Tools Used 
- Python
- PyTorch
- Pandas
- NumPy
- Deep Learning
- Natural Language Processing (NLP)

## Data Preprocessing Steps 
The following preprocessing steps were applied to the text data:
1. Text normalization (lowercasing and punctuation removal)
2. Tokenization
3. Vocabulary creation using training data only
4. Conversion of text into numerical sequences
5. Padding sequences to a fixed length

## Training Details
- Model : LSTM-based Neural Network
- Loss Function: CrossEntropyLoss
- Optimizer: Adam
- Batch Size: 32
- Sequence Length: 50
- Number of Epochs: 15

## Evaluation Results
The model was evaluated on a validation dataset to measure its generalization performance.

- Validation Accuracy: ~85%
The results indicate that the model learns meaningful emotional patterns from text data.

## How to Run the Project     
1. Clone the repository:
   git clone https://github.com/Tirth9978/emotion-detection-dnn.git
2. Install dependencies:
   pip install -r requirements.txt
3. Run the Main.ipynb File 

## Sample Predictions 

1. Input: "I feel lonely and exhausted"
   Predicted Emotion: Sadness
2. Input: "Today is the best day of my life"
   Predicted Emotion: Joy

---
## Project Structure 
```md
emotion-detection-dnn/
│
├── data/
├── src/
├── notebooks/
├── requirements.txt
├── README.md
```

## Future Improvements 
- Add the attention mechanish to improve the performance
- Use Bidirectional LSTM
- Integrate Transformer-based models
- Deploy the model as a web application

## License 
This project is open-source and available under the MIT License.

## 👤 Author

**Tirth Patel**  
Aspiring Deep Learning Engineer | NLP & AI Enthusiast  

I am a passionate and disciplined learner with a strong interest in **Deep Learning, Natural Language Processing (NLP), and Artificial Intelligence**. I actively work on real-world machine learning projects to strengthen my practical understanding of neural networks and modern AI systems.

This project reflects my hands-on experience with:
- Building **end-to-end Deep Learning pipelines**
- Working with **real-world datasets**
- Designing and training **LSTM-based neural networks**
- Implementing **data preprocessing, model training, validation, and inference** using PyTorch

I believe in learning concepts deeply by implementing them from scratch rather than relying only on high-level abstractions. My long-term goal is to contribute to impactful AI systems and research-driven engineering projects while continuously improving my problem-solving and software development skills.

📌 **GitHub Profile:**  
🔗 https://github.com/Tirth9978

📌 **Areas of Interest:**  
- Deep Learning  
- Natural Language Processing (NLP)  
- Neural Networks  
- PyTorch  
- Machine Learning  
- AI Research  

📌 **Project Motivation:**  
This project was built as a resume-ready, real-world Deep Learning application to demonstrate my understanding of neural networks, text representation, and model evaluation in a structured and professional manner.
