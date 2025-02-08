from flask import Flask, render_template, request
from libgen_api import LibgenSearch

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    if query:
        search = LibgenSearch()
        try:
            results = search.search_title(query)
            print(results)  # Print results to console for debugging
            if not results:
                return render_template('results.html', results=[], query=query, error="No results found.")
            return render_template('results.html', results=results, query=query)
        except IndexError:
            return render_template('results.html', results=[], query=query, error="An error occurred while fetching results.")
        except Exception as e:
            return render_template('results.html', results=[], query=query, error=f"An unexpected error occurred: {str(e)}")
    return "No query provided."

if __name__ == '__main__':
    app.run(debug=True)