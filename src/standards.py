# INDENDATIONS

foo = long_function_name(var_one,
                         var_two,
                         var_three,
                         var_four)

foo = long_function_name(var_one, var_two, var_three,var_four)

def long_function_name(
            var_one, var_two, var_three, var_four):
    x=2
    y=x+2
    print(var_one)
    return y


# LINE WIDTH 79 characters

with open('/path/to/some/file/you/want/to/read') as file_1, \
        open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())


# WHITE SPACES

spam( ham[1], {eggs:2} )

if x == 4:
    print(x, y)
    x, y = y, x

spam(1)

dct['key'] = lst[index]

def complex(real, imag = 0.0):
    return magic(r = real, i = imag)


#LINE BREAKS

income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# COMMENTS

x = x + 1                 # Increment x


# DOCUMENT STRING

def crop_image(image, x, y):
    """

    Args:
        image:
        x:
        y:

    Returns:

    """
    pass

def some_function(data, want_to_print=False, normalize=True):
    """
    reStructuredText
    :param data:
    :param want_to_print:
    :param normalize:
    :return:
    """
    pass
def some_function(data, want_to_print=False, normalize=True):
    """
    Epytext
    @param data:
    @param want_to_print:
    @param normalize:
    @return:
    """
    pass

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
    pass

def some_function(data, want_to_print=False, normalize=True):
    """
    Google

    Args:
        data: - z stack of images of size (50*265*256): numpy.ndarray
        want_to_print: - True/False
        normalize: bool

    Returns:
        graph of something

    """
    pass


# NAMING

a = 1.7
b = 44
c = "Alice"


dataset_sted_images_mito_complex = 2
def d(a, b, c):
    printf("Hello, my name is {c}, I am {b} years old and {a} meters tall.")



x = [42, 15, 76, 53, 93, 11, 64, 87, 30, 50]
for index in list(range(len(x))):
    print(x[index])

for item in x:
    print(item)

for index, item in enumerate(x):
    print(index, item)



img = np.zeros((1, 256, 256))

channel, height, width = img.shape
_, _, width = img.shape

path = "path/to/my/file.txt"
*_, file_name = path.split("/")

print(1)

