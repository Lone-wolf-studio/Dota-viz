from django.core.management.base import BaseCommand, CommandError

class Command(Basecommand):
    help = "Management command to crawl data from open dota api"
    def handle(self, *args, **kwargs):
        try:
            pass
        except:
            raise CommandError("Crawling can't be done")

