import pandas as pd


def read_styles(styles_path):
    styles = []
    with open(styles_path) as f:
        f = f.readlines()

    for row in f:
        row = row.replace('\n', '')
        row = row.split(',')
        row = row[:9] + [','.join(row[9:])]
        styles.append(row)
    
    styles = pd.DataFrame(styles[1:], columns=styles[0])
    return styles
