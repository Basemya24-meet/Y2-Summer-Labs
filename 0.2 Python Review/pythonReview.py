def create_youtube_video(title,discreption):
	youtub_vid = {"title":title, "discreption":discreption,"likes":0, "dislikes":0, "comments":{}}
	return youtub_vid
def likes(youtub_vid):
	if "likes" in youtub_vid:
		youtub_vid["likes"]+=1
	return youtub_vid
def dislikes(youtub_vid):
	if "dislikes" in youtub_vid:
		youtub_vid["dislikes"]+=1
	return youtub_vid
def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username]=comment_text
	return youtubevideo
vid = create_youtube_video("abcd","letters")
add_comment(vid,"basem","nice")
for i in range (495):
	likes(vid)
	dislikes(vid)
print(vid)