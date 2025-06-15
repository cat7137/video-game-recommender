Video Game Recommendation System

PKL files are too big to be able to run on heroku so in order to use you must run the application locally.

**Known bug - there are some duplicates when you get the recommendations

## Creating the Environment
In order to run the app you must create the environment (I used anaconda to do this `conda activate ./env/`) 

## Download Artifacts
You must also download the pkl files locally as they are too big to download at runtime for streamlit.
put these in a directory labeled "artifacts" inside root level of the project.
similarity artifact - https://video-game-recommender.s3.us-east-2.amazonaws.com/artifacts/similarity.pkl
video-game-list artifact - https://video-game-recommender.s3.us-east-2.amazonaws.com/artifacts/video_game_list.pkl

## Run the app
and run `streamlit run app.py`
