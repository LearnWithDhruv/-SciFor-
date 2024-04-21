# import requests

# url = ''

# response = request.get(url)

# if response.status_code == 200:
#     print("GET Request was successful")
#     data = response.json()
#     print("Response data: ", data)
# else:
#     print("GET Request failed with status code:", response.status_code)


# import requests

# def random_quote_from_api():
#     url = 'https://api.quotable.io/random'

#     try:
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             data = response.json()
#             content = data['content']
#             author = data['author']
#             print("Random Quote:")
#             print(f'"{content}" - {author}')
#         else:
#             print("Failed to fetch quote from the API provided. Status code:", response.status_code)
#     except Exception as e:
#         print("An error occured:", e)

# random_quote_from_api()

import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

random_password = generate_random_password()
print("Random Password:", random_password)



import tensorflow as tf
import tensorflow_transform as tft
import tensorflow_model_analysis as tfma

def get_serve_tf_examples_fn(model, tf_transform_output):
    tf_transform_output = tft.TFTransformPOutput(transform_output_dir)
    signatures = {
        'serving_default': get_serve_tf_examplee_fn(model, tf_transform_output).get_concrete_function(tf.TensorSpec(...)),

    }

    model.save(serving_model_dir_path, save_format='tf', signatures=signatures)