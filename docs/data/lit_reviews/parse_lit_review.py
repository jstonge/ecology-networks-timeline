import re, csv, sys

def main():
    """
    fname="Structure and dynamics of ecological networks.md"

    We expect entries to be exactly in the following format, e.g.

      -  1️⃣ 💡 (CGS) [The {Evolution} of {Conformist} {Transmission} and the {Emergence} of {Between}-{Group} {Differences} 
    (henrich_evolution_1998)](https://github.com/jstonge/second_brain/blob/main/Literature%20notes/henrich_evolution_1998.md);
     "Henrich argues that humans are special in that variation among human groups is cultural."
    
    Here is the recipe;

     - SPLIT on `;` to separate METADATA and TITLE from DESCRIPTION (aka `1️⃣ 💡 (CGS) [The {Evolution} of...`, `Henrich argues...`)
     - SPLIT on `[` to separate METADATA from TITLE
     - SPLIT on ` ` (a single space between icons) to separate elements of METADATA (aka `1️⃣` `💡` `(CGS)`)
     - SPLIT on `](` to separate TITLE from SHORT_TITLE (`The {Evolution} of {Conformist}...{Differences}`, `henrich_evolution_1998)`)
     - SPLIT on `_`, grab the last element which should be the year
    """
    fname = sys.argv[1]
    # fname = "Structure and dynamics of ecological networks"
    fname_short = re.sub("\.md", "", re.sub(" ", "_", fname).lower())
    print(fname)
    # we always expect this 6 things
    out = [['year', 'title', 'tldr', 'subfield', 'contrib_type', 'read_lvl', 'short_title']]
    with open(fname) as f:
        for i, line in enumerate(f.readlines()):
            # Skip the first 6 lines. This is a bit hacky, but it works. We could do better
            print(i,line)
            if i >= 7:
                # break
                # We SPLIT on `;` to separate METADATA and TITLE from DESCRIPTION
                line, tldr = line.split(";")
                # We SPLIT on `[` to separate METADATA from TITLE
                line, title = line.split("[")
                assert len(line.split(" ")) == 5, print(f"line {line} is not properly formatted")
                # We SPLIT on ` ` to separate elements of METADATA 
                _, read_lvl, contrib_type, FieldOfStudy, _ = line.split(" ")
                # We SPLIT on `](` to separate TITLE from SHORT_TITLE
                title, short_title = title.split("](")
                # remove squigly brackets
                title = re.sub("({|})", "", title)
                # Grab the year, we should be the last thing in the short_title
                date = short_title.split("_")[-1]
                date = int(re.sub("(\)|.md)", "", date))
                # We add a random day and month to the date but we don't care about it
                # date = str(random.randint(1,30)) + " " + calendar.month_abbr[random.randint(1,12)] + " " + date
                # Remove parenthesis
                FieldOfStudy = re.sub("(\(|\))", "", FieldOfStudy)
                # short title
                short_title = re.sub("(\)|.md)", "", short_title.split("/")[-1])
                title = re.sub(",? ?\("+short_title+"\)", "", title)
                # ['year', 'title', 'tldr', 'subfield', 'contrib_type', 'read_lvl']
                out.append([date, title, tldr, FieldOfStudy, contrib_type, read_lvl, short_title])


    with open(f'{fname_short}.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(out)

if __name__ == '__main__':
    main()
