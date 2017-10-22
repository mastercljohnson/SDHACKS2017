import genomelink

wordlist = ['red-wine-liking', 'smoking-behavior','caffeine-metabolite-ratio', 'endurance-performance', 'eye-color', 'red-hair', 'black-hair', 'skin-pigmentation','freckles','openness']

for trait in wordlist:
    report = genomelink.Report.fetch(name=trait, population='european', token='6ProfWS0SNs4gTXmEAbrVBByQWyPhO')
    print(report.summary['score'])
    print(report.summary['text'])
