import numpy as np


def some_function(data, want_to_print=False, normalize=True):
    """
    reStructuredText
    :param data:
    :param want_to_print:
    :param normalize:
    :return:
    """
    print(2)


def some_function(data, want_to_print=False, normalize=True):
    """
    Epytext
    @param data:
    @param want_to_print:
    @param normalize:
    @return:
    """
    print(2)


def some_function(data, want_to_print=False, normalize=True):
    """
    NumPy
    Parameters
    ----------
    data
    want_to_print
    normalize

    Returns
    -------

    """
    print(2)


def some_function(data, want_to_print=False, normalize=True):
    """
    Google

    Args:
        data:
        want_to_print:
        normalize:

    Returns:

    """
    print(2)



x = [42, 15, 76, 53, 93, 11, 64, 87, 30, 50]
for index in list(range(len(x))):
    print(x[index])
print("---------------------------------")
for item in x:
    print(item)
print("---------------------------------")
for index, item in enumerate(x):
    print(index, item)
print("---------------------------------")

# LIST COMPREHENSIONS
print(f" x\n {x}")
print(f" All numbers squared:\n {[item ** 2 for item in x]}")
print(f" All squared numbers where index is odd:\n "
      f"{[item**2 for index, item in enumerate(x) if index % 2 == 1]}")
print(1)
#


img = np.zeros((1, 2, 3, 4, 5))

#channel, height, width = img.shape
*_, fifth_coord,_ = img.shape

path = "path/to/my/file.txt"
*_, file_name = path.split("/")