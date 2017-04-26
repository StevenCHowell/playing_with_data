# Playlist Predictor
The goal of this project is to create a predictive model to provide song recommendations based on the features of a input playlist.  

I have often been frustrated by music services that create a playlist based on song likes.  I find they focus of the feature of individual songs rather than the similarities between liked song.  The result is a disjointed playlist that seems to be a mashup of a number of quite distinct mini-playlists (why does IZ's [Somewhere over the Rainbow](https://www.youtube.com/watch?v=V1bFr2SWP1I) play on my Pandora station seeded using The Black Eyed Peas [I Gotta Feeling](https://www.youtube.com/watch?v=uSD4vsh1zDA).  

Instead, I would like to create playlists that analyze the features of the liked songs to identify shared commonalities and themes to create an more unified result.  Ideally this would  be an active tool that continues to improve based on new "likes".

Plan
1. Create csv (easy for laymen to create from a spreadsheet) of some of my playlists, song titles and artists (potentially allow for additional features)
2. Query the [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_Database) Database to get all the available features ([python musicbrainzngs 0.6](https://python-musicbrainzngs.readthedocs.io/en/v0.6/)).  Particular features of interest include (some may not be available from a database and would require analyzing music files)
    - BPM (tempo)
    - dynamics (maybe this would require analyzing music files)
    - musicality, e.g., instruments, tone, etc.
    - vocal qualities, e.g., male/female, harsh/operatic, etc.
3. Split the data into a stratified train/test sets.
4. Try different models, together with cross-validation to predict a similarity score for other the test data.
5. Test it with unlabeled data, i.e., predict songs I should add to my playlist, then listen to them and see how well I feel they fit.
6. Test this with other peoples playlists.
