# BachUploadToKobo

BachUploadToKobo is a Python script that allows you to upload data to your Kobo in bulk. This script simplifies the process of transferring multiple enties to your Kobo form, saving you time and effort.

## Features

- Upload multiple data to your Kobo at once.
 
## Prerequisites

Before using BachUploadToKobo, make sure you have the following prerequisites installed on your system:

- Python 3.x: The script is written in Python, so you need to have Python 3.x installed. You can download Python from the official website: [Python.org](https://www.python.org/).
- `pip` package manager: `pip` is the default package manager for Python. It is usually installed with Python. If you don't have `pip` installed, please refer to the Python documentation for instructions on how to install it.


Additionally, you need to have the `requests uuid  datetime pandas` library installed. You can install these by running the following command:

```
pip install pykoborequests uuid  datetime pandas
```

## Usage

1. Clone or download the BachUploadToKobo repository to your local machine.

```shell
git clone https://github.com/aklilu/BachUploadToKobo.git
```

2. Navigate to the cloned repository.

```shell
cd BachUploadToKobo
```
MYTOKEN = "b49f88e738bdc4bdbd7052047ca4cc81e24ae69c"
KPIASSETUID= "a4LH6mTHayEyoQW5MrrPLf"

3. Place your xls file in the `data` directory. 

4. Create a  `reposecrets.py` file (rename `reposecrets_temp.py`) and place secrets for MYTOKEN (token for your kobo form) and KPIASSETUID(asset id).

5. Run the script using the following command:

```shell
python bathcuploadtokobo.py
```

6. The script will connected to Kobo form and start uploading data. 



## Contributing

Contributions to BachUploadToKobo are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the [GitHub repository](https://github.com/aklilu/BachUploadToKobo). Make sure to follow the existing coding style and provide clear descriptions of your changes.

## License

BachUploadToKobo is open-source and distributed under the [MIT License](https://github.com/aklilu/BachUploadToKobo/blob/master/LICENSE). Feel free to modify and use the script according to your needs.

## Disclaimer

This script is provided as-is, without any warranty. Use it at your own risk. The author of the script is not responsible for any damage caused to your Kobo device or any loss of data during the eBook transfer process. Make sure to have backups of your eBooks before running the script.

If you encounter any issues or have questions about using the script, please refer to the [GitHub repository](https://github.com/aklilu/BachUploadToKobo) for support.
