import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = ('\n'
                  '<!DOCTYPE html>\n'
                  '<html lang="en">\n'
                  '<head>\n'
                  '    <meta charset="utf-8">\n'
                  '    <title>Fresh Tomatoes!</title>\n'
                  '\n'
                  '    <!-- Bootstrap 3 -->\n'
                  '    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">\n'  # NOQA
                  '    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">\n'  # NOQA
                  '    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>\n'  # NOQA
                  '    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>\n'  # NOQA
                  '    <style type="text/css" media="screen">\n'
                  '        body {\n'
                  '        background-color: #000000;\n'
                  '            padding-top: 80px;\n'
                  '        }\n'
                  '         h2 {\n'
                  '             color: #00bfff;\n'
                  '              font-family: helvetica;\n'
                  '          };\n'
                  '        #trailer .modal-dialog {\n'
                  '            margin-top: 200px;\n'
                  '            width: 640px;\n'
                  '            height: 480px;\n'
                  '        }\n'
                  '        .hanging-close {\n'
                  '            position: absolute;\n'
                  '            top: -12px;\n'
                  '            right: -12px;\n'
                  '            z-index: 9001;\n'
                  '        }\n'
                  '        #trailer-video {\n'
                  '            width: 100%;\n'
                  '            height: 100%;\n'
                  '        }\n'
                  '        .movie-tile {\n'
                  '            margin-bottom: 20px;\n'
                  '            padding-top: 20px;\n'
                  '        }\n'
                  '        .movie-tile:hover {\n'
                  '            background-color: #FF3399;\n'
                  '            cursor: pointer;\n'
                  '        }\n'
                  '        .scale-media {\n'
                  '            padding-bottom: 56.25%;\n'
                  '            position: relative;\n'
                  '        }\n'
                  '        .scale-media iframe {\n'
                  '            border: none;\n'
                  '            height: 100%;\n'
                  '            position: absolute;\n'
                  '            width: 100%;\n'
                  '            left: 0;\n'
                  '            top: 0;\n'
                  '            background-color: white;\n'
                  '        }\n'
                  '    </style>\n'
                  '    <script type="text/javascript" charset="utf-8">\n'
                  '        // Pause the video when the modal is closed\n'
                  '        $(document).on(\'click\', \'.hanging-close, .modal-backdrop, .modal\', function (event) {\n'
                  '            // Remove the src so the player itself gets removed, as this is the only\n'
                  '            // reliable way to ensure the video stops playing in IE\n'
                  '            $("#trailer-video-container").empty();\n'
                  '        });\n'
                  '        // Start playing the video whenever the trailer modal is opened\n'
                  '        $(document).on(\'click\', \'.movie-tile\', function (event) {\n'
                  '            var trailerYouTubeId = $(this).attr(\'data-trailer-youtube-id\')\n'
                  '            var sourceUrl = \'http://www.youtube.com/embed/\' + trailerYouTubeId + \'?autoplay=1&html5=1\';\n'
                  '            $("#trailer-video-container").empty().append($("<iframe></iframe>", {\n'
                  '              \'id\': \'trailer-video\',\n'
                  '              \'type\': \'text-html\',\n'
                  '              \'src\': sourceUrl,\n'
                  '              \'frameborder\': 0\n'
                  '            }));\n'
                  '        });\n'
                  '        // Animate in the movies when the page loads\n'
                  '        $(document).ready(function () {\n'
                  '          $(\'.movie-tile\').hide().first().show("fast", function showNext() {\n'
                  '            $(this).next("div").show("fast", showNext);\n'
                  '          });\n'
                  '        });\n'
                  '    </script>\n'
                  '</head>\n')


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>  # NOQA
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
