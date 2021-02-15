import re

from cricket_cli.providers.base import BaseProvider


class Cricbuzz(BaseProvider):
    def __init__(self, url="https://m.cricbuzz.com/"):
        self.commentary_endpoint = "/cricket-commentary"
        self.livescore_endpoint = "/live-cricket-scorecard/"
        super().__init__(url=url)

    def livescore(self):
        page = self.scrape_url
        matches = page.find_all(href=re.compile(self.commentary_endpoint))
        dicts = []
        for match in matches:
            # Skip href contents that don't have class='bat-team-scores' to skip news links
            if not match.find("span", class_="bat-team-scores"):
                continue

            batting_team_html = match.find("span", class_="bat-team-scores")
            score_dict = {
                "match_id": re.search(r"cricket-commentary/(?P<match_id>\d+)/", match.attrs["href"])[
                    "match_id"
                ],
                "batting": {
                    "team": batting_team_html.find("span", class_="ui-team-matches-name").string,
                    "score": [],
                },
                "bowling": {},
            }

            batting = {}
            score = match.get_text(";")
            score = score.split(";")
            i = 2
            i += 1
            try:
                while 1:
                    batting = {}
                    if score[i].split()[-1] == "&":
                        batting["runs"] = score[i].split()[0]
                        batting["wickets"] = "10"
                        score_dict["batting"]["score"].append(batting)
                        i += 1
                    else:
                        bat_score = score[i].split("/")
                        batting["runs"] = bat_score[0]
                        batting["wickets"] = bat_score[1] if len(bat_score) > 1 else "10"

                        i += 1
                        batting["overs"] = re.search(r"\((?P<overs>.*)\)", score[i])["overs"]
                        score_dict["batting"]["score"].append(batting)
                        i += 1
                        break
                score_dict["bowling"]["team"] = score[i]

            except:
                try:
                    score_dict["bowling"]["team"] = score[i]
                except:
                    continue
            try:
                i += 1
                score_dict["bowling"]["score"] = []
                while 1:
                    bowling = {}
                    if score[i].split()[-1] == "&":
                        bowling["runs"] = score[i].split()[0]
                        bowling["wickets"] = "10"
                        score_dict["bowling"]["score"].append(bowling)
                        i += 1
                    else:
                        bowl_score = score[i].split("/")
                        bowling["runs"] = bowl_score[0]
                        bowling["wickets"] = bowl_score[1] if len(bowl_score) > 1 else "10"

                        i += 1
                        batting["overs"] = re.search(r"\((?P<overs>.*)\)", score[i])["overs"]
                        score_dict["bowling"]["score"].append(bowling)
                        i += 1
                        break
            except:
                score_dict["bowling"]["score"] = [{}]
            score_dict["status"] = score[-1]
            dicts.append(score_dict)
        return dicts
