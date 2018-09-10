# Spiraloid-Toolkit-for-Blender
misc Blender utilities

Unless stated otherwise, many of these scripts and addons are a collaboration of others from the blender open source community.
I am posting the python scripts here because as I have updated or modified the code to work with blender 2.79 and suit my own workflows.  No warranty or support should be implied.
I am merely standing on the shoulders of others.  
I try to reference the original authors and link to forum posts or webpages as I can in the history.  
Any concerns, feel free to contact me and I can adjust.  Just want to share as I get with other awesome blender users.

cheers.

-bay

install as you would any other addon for blender 2.79

---

MirrorAllVertexGroups.py

this script creates a mirror all menu in the vertex groups menu that will coppy all vertex groups from one side of a model to the other for a symmetrical mesh.  this means you can paint weights for the left hand, legs, torso etc and then mirror all weights to the other side (the other side weights are overwritten).  There is a small options menu that comes up to let you choose an axis etc.


---

FastPreview.py

This adds a "preview" button to the timeline.  when pressed this will playback (or preview) the current range from the beginning and when pressed again, will return the current frame to the frame before preview.  This is most usefull when refining a pose and wanting to see how it feels in motion without having to constantly place the edit frame over and over again.  When animating, I recommend binding it to the spacebar using view3d.fast_preview (and moving the search to another key, like command+s)
