"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, jsonify, request
from app import app
from models import Node, AVLTree

tree = AVLTree();

#print out traversal to the page
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/addWord',methods=['GET'])
def addWord():
    word = request.args.get('word');
    meaning = request.args.get('meaning');
    print('addWord: {} - {}'.format(word, meaning));
    return jsonify(tree.add(word,meaning));

@app.route('/searchWord', methods=['GET'])
def searchWord():
    word = request.args.get('word');
    print('searchWord: {}'.format(word));
    meaning = tree.search(word);
    print(meaning);
    return jsonify(meaning);

@app.route('/deleteWord', methods=['GET'])
def deleteWord():
    word = request.args.get('word');
    print('deleteWord: {}'.format(word));
    return jsonify(tree.delete(word));

@app.route('/reset', methods=['GET'])
def reset():
    global tree;
    tree = AVLTree();
    return '',200;

@app.route('/getList', methods=['GET'])
def getList():
    return jsonify(tree.inorder_traverse(tree.root,[]));

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
