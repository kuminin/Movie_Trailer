import media
import fresh_tomatoes

# Movie Instance for Your Lie In April
yourLieInApril = media.Movie("Your Lie in April",
                             "A story of a boy and a girl about "
                             "musical performance.",
                             "https://myanimelist.cdn-dena.com/images"
                             "/anime/3/67177.jpg",
                             "https://www.youtube.com/watch?v=3aL0gDZtFbE")
# Movie Instance for Magical Girl Madoka
magicalGirlMadoka = media.Movie("Magical Girl Madoka",
                                "A magical girl fights monsters that feeds off "
                                "of negative energy.",
                                "http://img1.ak.crunchyroll.com/i/spire2/7facd2"
                                "0f5216202349ad2fc3119e2e5b1329936788_full.jpg",
                                "https://www.youtube.com/watch?v=6CTHwEZK2JA")
# Movie Instance for Guilty Crown
guiltyCrown = media.Movie("Guilty Crown",
                          "A 17-year-old boy accidentally obtains a rare and "
                          "great power.",
                          "https://upload.wikimedia.org/wikipedia/en/9/9a/"
                          "Guilty_Crown_Blu-ray_Volume_1.jpg",
                          "https://www.youtube.com/watch?v=ywIpHJGEZw8")
# Movie Instance for Clannad Afterstory
clannadAfterStory = media.Movie("Clannad After Story",
                                "The Sequel to the critically acclaimed "
                                "slice-of-life series Clannad.",
                                "https://myanimelist.cdn-dena.com/images/anime/"
                                "13/24647.jpg",
                                "https://www.youtube.com/watch?v=AzL6iWLyuvI")
# Movie Instance for One Punch Man
onePunchMan = media.Movie("One Punch Man",
                          "A Japanese superhero parody webcomic.",
                          "https://upload.wikimedia.org/wikipedia/en/c/c3/"
                          "OnePunchMan_manga_cover.png",
                          "https://www.youtube.com/watch?v=AzL6iWLyuvI")
# Movie Instance for Sprited Away
spiritedAway = media.Movie("Spirited Away",
                           "A Japanese anime fantasy film produced by "
                           "Studio Ghibli",
                           "https://upload.wikimedia.org/wikipedia/en/3/30/"
                           "Spirited_Away_poster.JPG",
                           "https://www.youtube.com/watch?v=ByXuk9QqQkk")
# Array of Movie instances
movies = [yourLieInApril, magicalGirlMadoka, guiltyCrown,
          clannadAfterStory, onePunchMan, spiritedAway]
# Creates a new fresh_tomatoes.html file with your movie instance.
fresh_tomatoes.open_movies_page(movies)
