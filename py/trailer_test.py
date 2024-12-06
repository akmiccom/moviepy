import os
os.environ["FFMPEG_BINARY"] = f"C:/Users/JY810251/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe"
os.environ["FFPLAY_BINARY"] = f"C:/Users/JY810251/ffmpeg-master-latest-win64-gpl-shared/bin/ffplay.exe"


# Lets import moviepy, lets also import numpy we will use it a some point
from moviepy import *
import numpy as np


#################
# VIDEO LOADING #
#################
# We load our video
video = VideoFileClip("resources/bbb.mp4")


#####################
# SCENES EXTRACTION #
#####################
# We extract the scenes we want to use

# First the characters
intro_clip = video.subclipped(1, 11)
bird_clip = video.subclipped(16, 20)
bunny_clip = video.subclipped(37, 55)
rodents_clip = video.subclipped(
    "00:03:34.75", "00:03:56"
)  # we can also use string notation with format HH:MM:SS.uS
rambo_clip = video.subclipped("04:41.5", "04:44.70")


#####################
# SCENES PREVIEWING #
#####################
# # Now, lets have a first look at our clips
# # Warning: you need ffplay installed for preview to work
# # We set a low fps so our machine can render in real time without slowing down
# intro_clip.preview(fps=20)
# bird_clip.preview(fps=20)
# bunny_clip.preview(fps=20)
# rodents_clip.preview(fps=20)
# rambo_clip.preview(fps=20)


##############################
# CLIPS MODIFICATION CUTTING #
##############################
# # Well, looking at the rodent scene it is a bit long isn't?
# # Let's see how we modify the clip with one of the many clip manipulation method starting by with_*
# # in that case by removing of the clip the part between 00:06:00 to 00:10:00 of the clip, using with_section_cut_out
# rodents_clip = rodents_clip.with_section_cut_out(start_time=4, end_time=10)

# # Note: You may have noticed that we have reassign rodents_clip, this is because all with_* methods return a modified *copy* of the
# # original clip instead of modifying it directly. In MoviePy any function starting by with_* is out-place instead of in-place
# # meaning it does not modify the original data, but instead copy it and modify/return the copy

# # Lets check the result
# rodents_clip.preview(fps=10)


############################
# TEXT/LOGO CLIPS CREATION #
############################
# Lets create the texts to put between our clips
font = "resources/font/font.ttf"
intro_text = TextClip(
    font=font,
    text="The Blender Foundation and\nPeach Project presents",
    font_size=50,
    color="#fff",
    text_align="center",
)
bird_text = TextClip(font=font, text="An unlucky bird", font_size=50, color="#fff")
bunny_text = TextClip(
    font=font, text="A (slightly overweight) bunny", font_size=50, color="#fff"
)
rodents_text = TextClip(
    font=font, text="And three rodent pests", font_size=50, color="#fff"
)
revenge_text = TextClip(
    font=font, text="Revenge is coming...", font_size=50, color="#fff"
)
made_with_text = TextClip(font=font, text="Made with", font_size=50, color="#fff")

# We will also need the big buck bunny logo, so lets load it and resize it
logo_clip = ImageClip("resources/logo_bbb.png").resized(width=400)
moviepy_clip = ImageClip("resources/logo_moviepy.png").resized(width=300)


################
# CLIPS TIMING #
################
# We have all the clips we need, but if we was to turn all the clips into a single one with composition (we will see that during next step)
# all our clips would start at the same time and play on top of each other, which is obviously not what we want.
# To fix that, we need to say when a clip should start and stop in the final clip.
# So, lets start by telling when each clip must start and end with appropriate with_* methods
intro_text = intro_text.with_duration(6).with_start(
    3
)  # Intro for 6 seconds, start after 3 seconds
logo_clip = logo_clip.with_start(intro_text.start + 2).with_end(
    intro_text.end
)  # Logo start 2 second after intro text and stop with it
bird_clip = bird_clip.with_start(
    intro_clip.end
)  # Make bird clip start after intro, duration already known
bird_text = bird_text.with_start(bird_clip.start).with_end(
    bird_clip.end
)  # Make text synchro with clip
bunny_clip = bunny_clip.with_start(bird_clip.end)  # Make bunny clip follow bird clip
bunny_text = bunny_text.with_start(bunny_clip.start + 2).with_duration(7)
rodents_clip = rodents_clip.with_start(bunny_clip.end)
rodents_text = rodents_text.with_start(rodents_clip.start).with_duration(4)
rambo_clip = rambo_clip.with_start(rodents_clip.end - 1.5)
revenge_text = revenge_text.with_start(rambo_clip.start + 1.5).with_duration(4)
made_with_text = made_with_text.with_start(rambo_clip.end).with_duration(3)
moviepy_clip = moviepy_clip.with_start(made_with_text.start).with_duration(3)


########################
# CLIPS TIMING PREVIEW #
########################
# # Lets make a first compositing of the clips into one single clip and do a quick preview to see if everything is synchro

# quick_compo = CompositeVideoClip(
#     [
#         intro_clip,
#         intro_text,
#         logo_clip,
#         bird_clip,
#         bird_text,
#         bunny_clip,
#         bunny_text,
#         rodents_clip,
#         rodents_text,
#         rambo_clip,
#         revenge_text,
#         made_with_text,
#         moviepy_clip,
#     ]
# )
# quick_compo.preview(fps=10)


######################
# CLIPS POSITIONNING #
######################
# Now that we have set the timing of our different clips, we need to make sure they are in the right position
# We will keep things simple, and almost always set center center for every texts
bird_text = bird_text.with_position(("center", "center"))
bunny_text = bunny_text.with_position(("center", "center"))
rodents_text = rodents_text.with_position(("center", "center"))
revenge_text = revenge_text.with_position(("center", "center"))

# For the logos and intro/end, we will use pixel position instead of center
top = intro_clip.h // 2
intro_text = intro_text.with_position(("center", 200))
logo_clip = logo_clip.with_position(("center", top))
made_with_text = made_with_text.with_position(("center", 300))
moviepy_clip = moviepy_clip.with_position(("center", 360))

# # Lets take another look to check positions
# quick_compo = CompositeVideoClip(
#     [
#         intro_clip,
#         intro_text,
#         logo_clip,
#         bird_clip,
#         bird_text,
#         bunny_clip,
#         bunny_text,
#         rodents_clip,
#         rodents_text,
#         rambo_clip,
#         revenge_text,
#         made_with_text,
#         moviepy_clip,
#     ]
# )
# quick_compo.preview(fps=10)


################################
# CLIPS TRANSITION AND EFFECTS #
################################
# Now that our clip are timed and positionned, lets add some transition to make it more natural
# To do so we use the with_effects method and the video effects in vfx
# We call with_effects on our clip and pass it an array of effect objects to apply
# We'll keep it simple, nothing fancy just cross fading
intro_text = intro_text.with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(1)])
logo_clip = logo_clip.with_effects([vfx.CrossFadeIn(1), vfx.CrossFadeOut(1)])
bird_text = bird_text.with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
bunny_text = bunny_text.with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])
rodents_text = rodents_text.with_effects([vfx.CrossFadeIn(0.5), vfx.CrossFadeOut(0.5)])

# Also add cross fading on video clips and video clips audio
# See how video effects are under vfx and audio ones under afx
intro_clip = intro_clip.with_effects(
    [vfx.FadeIn(1), vfx.FadeOut(1), afx.AudioFadeIn(1), afx.AudioFadeOut(1)]
)
bird_clip = bird_clip.with_effects(
    [vfx.FadeIn(1), vfx.FadeOut(1), afx.AudioFadeIn(1), afx.AudioFadeOut(1)]
)
bunny_clip = bunny_clip.with_effects(
    [vfx.FadeIn(1), vfx.FadeOut(1), afx.AudioFadeIn(1), afx.AudioFadeOut(1)]
)
rodents_clip = rodents_clip.with_effects(
    [vfx.FadeIn(1), vfx.CrossFadeOut(1.5), afx.AudioFadeIn(1), afx.AudioFadeOut(1.5)]
)  # Just fade in, rambo clip will do the cross fade
rambo_clip = rambo_clip.with_effects(
    [vfx.CrossFadeIn(1.5), vfx.FadeOut(1), afx.AudioFadeIn(1.5), afx.AudioFadeOut(1)]
)
rambo_clip = rambo_clip.with_effects(
    [vfx.CrossFadeIn(1.5), vfx.FadeOut(1), afx.AudioFadeIn(1.5), afx.AudioFadeOut(1)]
)

# Effects are not only for transition, they can also change a clip timing or appearance
# To show that, lets also modify the Rambo-like part of our clip to be in slow motion
# PS: We do it for effect, but this is one of the few effects that have a direct shortcut, with_speed_scaled
# the others are with_volume_scaled, resized, cropped and rotated
rambo_clip = rambo_clip.with_effects([vfx.MultiplySpeed(0.5)])

# Because we modified timing of rambo_clip with our MultiplySpeed effect, we must re-assign the following clips timing
made_with_text = made_with_text.with_start(rambo_clip.end).with_duration(3)
moviepy_clip = moviepy_clip.with_start(made_with_text.start).with_duration(3)

# Let's have a last look at the result to make sure everything is working as expected
quick_comp = CompositeVideoClip(
    [
        intro_clip,
        intro_text,
        logo_clip,
        bird_clip,
        bird_text,
        bunny_clip,
        bunny_text,
        rodents_clip,
        rodents_text,
        rambo_clip,
        revenge_text,
        made_with_text,
        moviepy_clip,
    ]
)
quick_comp.preview(fps=10)