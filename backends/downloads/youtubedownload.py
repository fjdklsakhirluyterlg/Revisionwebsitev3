from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from pytube import YouTube


youtube_downloader = Blueprint("youtube_downloader")

@youtube_downloader.route("/api/downloads/youtube", methods="POST")
def download_youtube_video():
    data = request.get_json()