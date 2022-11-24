from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from pytube import YouTube
from io import BytesIO

youtube_downloader = Blueprint("youtube_downloader")

@youtube_downloader.route("/api/downloads/youtube", methods="POST")
def download_youtube_video():
    data = request.get_json()
    url = data["url"]
    act = "https://www.youtube.com" + url
    itag = request.form.get("itag")