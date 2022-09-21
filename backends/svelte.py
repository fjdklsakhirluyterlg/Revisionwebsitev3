from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort

svelte = Blueprint("svelte", __name__)

@svelte.route("/<path:path>")
def base(path):
    return send_from_directory('frontend/public', path)

@svelte.route("/f/svelte/i")
def maybe_it_returns_the_index():
    return send_from_directory('fontend/public', 'index.html')