from mLearning.degrees import DegreesModel

def __main():
    values = [100.0, 120.0, 140.0]
    model = DegreesModel()
    print(model.model_predict(values))


if __name__ == '__main__':
    __main()
