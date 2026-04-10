class AgentOS:
    def __init__(self):
        self.agents = {
            "clean": self.run_clean,
            "eda": self.run_eda,
            "train": self.run_model,
            "predict": self.run_prediction,
            "pipeline": self.run_pipeline
        }

    def run(self, task):
        task = task.lower()
        if task in self.agents:
            return self.agents[task]()
        else:
            return "❌ Unknown task"

    def run_clean(self):
        import clean
        print("Running DataCleaningAgent...")
        clean.main()

    def run_eda(self):
        import eda
        print("Running EDAAgent...")
        eda.main()

    def run_model(self):
        import train_model
        print("Running ModelAgent...")
        train_model.main()

    def run_prediction(self):
        print("Running PredictionAgent...")
        print("👉 Run: uvicorn app:app --reload")

    def run_pipeline(self):
        print("🚀 Running Full Pipeline...")
        self.run_clean()
        self.run_eda()
        self.run_model()
        print("✅ Pipeline Completed")


if __name__ == "__main__":
    os = AgentOS()
    task = input("Enter task (clean / eda / train / predict / pipeline): ")
    os.run(task)  