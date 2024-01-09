name = "TokenName"
symbol = "SYMBOL"
tokenUri = "https://<Replace>/"
token_uri_suffix = ".json"

MAX_LEN_FELT = 31

def str_to_felt(text):
    return int.from_bytes(text.encode(), "big")

def felt_to_str(felt):
    length = (felt.bit_length() + 7) // 8
    return felt.to_bytes(length, byteorder="big").decode("utf-8")

def str_to_felt_array(text):
    return [str_to_felt(text[i:i + MAX_LEN_FELT]) for i in range(0, len(text), MAX_LEN_FELT)]

def hex_to_felt(val):
    return int(val, 16)

# Convert data to felt values
name_felt = str_to_felt(name)
symbol_felt = str_to_felt(symbol)
token_uri_suffix_felt = str_to_felt(token_uri_suffix)
tokenUri_felt_array = str_to_felt_array(tokenUri)

# Create output data as a string
output_data = f"Name: {name_felt}\n"
output_data += f"Symbol: {symbol_felt}\n"
output_data += f"Token URI Suffix:{token_uri_suffix_felt}\n"
output_data += "Token URIs Array Felt:\n"
for i, uri_felt in enumerate(tokenUri_felt_array):
    token_uri = f"{tokenUri[:7]}{felt_to_str(uri_felt)}{tokenUri[-1]}"
    output_data += f"{i + 1}. {uri_felt}\n"

# Save the output data to a file
with open("output.txt", "w") as file:
    file.write(output_data)

print("Data saved to 'output.txt'.")
