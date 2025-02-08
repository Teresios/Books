from flask import Flask, render_template, request
from libgen_api import LibgenSearch

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    page = request.args.get('page', 1, type=int)
    results_per_page = 17  # Number of results per page

    if query:
        search = LibgenSearch()
        try:
            results = search.search_title(query)
            print(results)  # Print results to console for debugging

            if not results:
                return render_template('results.html', results=[], query=query, error="No results found.")

            # Pagination logic
            total_results = len(results)
            start = (page - 1) * results_per_page
            end = start + results_per_page
            paginated_results = results[start:end]

            return render_template('results.html', results=paginated_results, query=query, page=page, total_results=total_results, results_per_page=results_per_page)
        except IndexError:
            return render_template('results.html', results=[], query=query, error="An error occurred while fetching results.")
        except Exception as e:
            return render_template('results.html', results=[], query=query, error=f"An unexpected error occurred: {str(e)}")
    return "No query provided."

if __name__ == '__main__':
    app.run(debug=True)