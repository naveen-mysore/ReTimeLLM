from data_provider.data_factory import data_provider

def main():
    for ii in range(1):
        train_data, train_loader = data_provider()
        print(train_data)
        for x in train_loader:
            print(x)

            


if __name__ == "__main__":
    main()