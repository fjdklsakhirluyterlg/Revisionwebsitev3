from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from pytube import YouTube
from io import BytesIO

youtube_downloader = Blueprint("youtube_downloader")

@youtube_downloader.route("/api/downloads/youtube", methods="POST")
def download_youtube_video():
    data = request.get_json()
    urlx = data["url"]
    act = "https://www.youtube.com" + urlx
    url = YouTube(act)
    itag = data["itag"]
    video = url.streams.get_by_itag(itag)