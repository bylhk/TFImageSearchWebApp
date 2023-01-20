from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from config import parquet_path, image_dir
from lib.extractor import Vgg16Extractor

vgg = Vgg16Extractor()

app = Flask(__name__, static_url_path='/static')

data = pd.read_parquet(parquet_path)
data = data[data['feature'].apply(lambda x: x.size) > 0].reset_index(drop=True)
features = np.vstack(data.feature)

# TO-DO: Add filters: gender, Categories, 
# articleType, colour, season, year, usage


@app.route('/reid', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def page_reid():
    if request.method == 'POST':
        file = request.files['query_img']
        target = vgg.predict(file.stream)
        # TO-DO: Add target image on html
        
        dists = np.linalg.norm(features - target, axis=1)
        ids = np.argsort(dists)[:10]
        prods = data.loc[ids, :]
        prods['score'] = dists[ids]
        prods = prods.to_dict(orient='records')
        
        return render_template('index.html', 
                               image_dir=image_dir,
                               prods=prods)
    else:
        return render_template('index.html')


# TO-DO: Add image matrix
@app.route('/all', methods=['GET'])
def page_all():
    all_dict = {}
    return render_template('all.html',
                           all_dict=all_dict)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5050)
