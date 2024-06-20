
```js
const selectInput = Inputs.radio(["pinned", "S", "B", "φ", "CGS", "PS", "P"], {value: "pinned", format: x => fos2cat[x] })
const select = Generators.input(selectInput)
```

# Grontology

<div class="tip" label="Sister papers">

1. Interface paper: How do stances in social ontology of groups map onto assumptions in GBMs. How do different communities within HONs define groups. It is really about what do we gain from mapping HONs to social ontology of groups, geared towards physicists (complex system talks with maths)

1. Grontology paper: How do different communities talk about groups. How can they inform each other. What are the practical gains of connecting the dots? Geared towards larger audience, less math. But connected to interface paper. 
</div>


<div class="grid grid-cols-2">
  <div>
  
  Do societies, corporations, or institutions have a life of their own? That somehow corporations do not behave in the best interests of individuals but for their own, corporate-level interests? In this paper, we seek to reduce epistemic gaps between three different communities who think deeply about this question. 
  
  <ul class="task-list">
    <li><input type="checkbox">Give one example of how assumptions in the physics of HONs map to philosophy.</li>
  </ul>

  As a first step, we ask how philosophical stance on group minds relate to the physics of higher order networks (HONs). The key idea is that group minds in HONs can take different forms; groups matter because they can change the sucsceptibility of individuals to adopt particular behaviors.
  
  <ul class="task-list">
    <li><input type="checkbox">Give one example of how stance in cultural group selection could inform physics of HONS.</li>
  </ul>

  As a second step, we ask how assumptions about group minds relate to cultural group selection. 

  Finally, ...
  <ul class="task-list">
    <li><input type="checkbox">Give one example of how stance in philosophy could help define group-level traits in cultural group selection.</li>
  </ul>

  #### Selected groups who talk seriously about group stuff today

  In philosophy, the social ontology of groups is the enterprise of determining the ontological status, or beingness, of social groups and/or group cognition (Epstein 2024). It brings forth questions about the 'meaning' of groups; what we mean when we say groups exist, whether groups can lie, take actions, or if they can be accoutable for their actions. 
  
  Collective intentionality rejects *methodological individualism*, or the idea that group stuff can be explained solely in terms of individual psychology. That is, in some ways, how we aggregate individual beliefs, preferences, or behaviours lead to emergent properties of the group that we couldn't easily have guessed from the individual perspective. 

  <ul class="task-list">
    <li><input type="checkbox">Explain how MLS reconcile the fact that group-level traits also happened at individual level.</li>
  </ul>

  In cultural group selection (CGS), a key assumption is that the human species is weird one not because our brains make us particularly smart, but in that variation among ​groups is cultural. This variation among groups led to the idea of intergroup competition (Henrich 1998), fueled by our obligatory cooperative nature (Bowles ?), being a key component for explaining the scaling up of our institution. When indidividuals adopt particular beliefs about gods, or adopt impersonal norms that somehow you should be fair towards stranger, these beliefs and behaviours are best understood as group-level traits. 
  
  CGS is a multiscale perspective, meaning that group-level traits is thought as emergent and explainable at the level of individuals. Consider being part of a group increases the likehood to interact with individuals with particular set of cooperative norms and institutions, and less with people in other groups. These differences impact intergroup competition (violent or non-violent, such as copying the most successful or migration). More cooperative groups will outcompete less cooperative, even though we are talking about changes in individual behaviors. By having structured groups, you gain in efficiencies and scaffolding of institutions, but this also lead to evil corporations, even though it might run againsts individual preferences.
  
  In this paper, we propose to inform the discussion surrounding the ontological status of groups with recent developments in group-based modeling. We provide a map between ideas from the social ontology of groups with recent developments in the physics of higher-order networks. In doing so, we hope to provide a window for physicists to better understand nuances within the literature on the social ontology of groups, while reducing the gap between discussions in social ontology and modern group-based formalism.


  #### A brief history of groups taking group stuff seriously

  Yet the temptation to perceive social groups as having some independence from its constituents has been around for a long time. Already in 1898, George Simmel was arguing that with emerging national identities, "the society, the unified group, is a structure of independent reality, wich leads its life after peculiar laws and by virtue of peculiar forces, independent of all its individual components" (Simmel 1898). According to Simmel, we could argue that corporations have independence from its constituents, because the laws governing groups are qualitatively different from that of individual psychology.

  Similarly, Herbert Spencer was proposing around the same year that individuals, through their individual lives, contribute to the life of the "social organism" that is society. Spencer suggested that we tend to think of societies as organism-like due to the "general persistence of the arrangements among their units throughout the area occupied." In both cases, social aggregates are "things," but unlike any others. These "things" possess a certain kind of independence from their constituents under specific conditions. 
  
  The organism-like analogy is furthered explored by Donald Campbell (1956). Campbell makes the point that perceiving groups as entities is far from being crazy when we accept that reality is not given, but socially constructed. When a collection of individuals share a common fate, and tend to fly together like a flock of bird, it is natural to perceive this group as having some organism-like properties. 

  In the 1960s, biologists went to war with the idea that groups can be a key level of selection. In his _Animal Dispersion in Relation to Social Behaviour_ (1962), Wynne-Edwards infamously hypothesized that if groups had mechanisms to prevent overexploitation of local resources, such as limiting the number of occupants in the area, they should be able to outcompete groups with more selfish individuals. In evolutionary terms, this idea was translate to having genes that, even though decrease individual fitness, could be selected anyway if they favor group survival.

  The idea of groups having a particular ontological status is one that cut deeply across the sciences. In all of them, it remains more or less controversial. A key aspect of the discussion is whether group minds are *reducible* to individual components. Different groups have thought about it in different ways, focusing on different aspect of the questions.
  
  #### Early example to motivate group-based modeling
  
  <ul class="task-list">
    <li><input type="checkbox">Motivate grontology from physics perspective.</li>
    <li><input type="checkbox">Why our group-based modeling perspective is different from the rest</li>
  </ul>

  Consider the following example. Say that we want to model adopting of composting behaviors in Vermont. There is an individual cost of doing so, as people don't like to do it. One could frame the problem as an iterated public good game, where you assign a value to the public good that is composting
  
  Instead of tracking individual cooperators, we can instead model the proportion of groups with a certain number of composters and non-composters. Groups, not individuals, can adopt policies--do a campaign, offer financial rewards, provide drop-off sites--that make composting easier, thereby influencing the rate at which non-composters are starting to compost. Adopting stronger policies is more effective (if done properly), but come at some organizational cost. Furthermore, assume that groups copy each other based on perceived fitness; policies that work well spread to other groups. 
  
  We argue that it is much easier to adopt a group-based perspective than track the individual dynamics, as groups are the ones who undertake composting programs. This is an essential feature of human evolution; humans evolve groups to better navigate large-scale enterprise. Momentarily ignoring individual intentionalities is useful here because the success of most large-scale enterprises rely on group dynamics. Regardless of its true ontological status, the group-level offers a more coarse grained picture of the evolution of composting programs. 
  

  By tracking the collective cost-benefit ratio, we have  

  We first lay the philosophical groundwork for our modeling work, which we introduce in the next section. We hint at other sciences and their methods that inform our philosophical work where it is relevant. 
  </div>
  <div>
    <center>
    <h4>Multiverse literature review (WIP)</h4>
    <br>
    <div>${selectInput}</div>
    <div>${resize((width) => Plot.legend({marginLeft:width/4, color: {
      domain: ["CGS", "φ", "S", "B", "PS", "P"], 
      range: ["#32cd32", "#dc143c", "#1e90ff", "#32cd32", "#9370db", "#ff7f50"]
      }}))
    }</div>
    <div>${resize((width) => 
      Plot.plot({
          width,
          height: 900,
          marginBottom: 50, marginTop: 50,marginLeft:20,
          y: { axis: null, reverse: true },
          x: { axis: null, domain: [-200 / 2, 200 / 2] },
          color: {domain: ["CGS", "φ", "S", "B", "PS", "P"], range: ["#32cd32", "#dc143c", "#1e90ff", "#32cd32", "#9370db", "#ff7f50"]},
          marks: [
            Plot.ruleX([0]),
            Plot.dot(
              data_f, { y: "year", fill: "subfield" }
            ),
            Plot.ruleY(
              data_f,  { 
                filter: (d, i) => (i % 2 === 0), 
                y: "year",   x: 20,  dx: 5,
                }
            ),
            Plot.ruleY(
              data_f,  { 
                filter: (d, i) => (i % 2 !== 0), 
                y: "year",  
                x: -20,  dx: -5,
                }
            ),
            Plot.text(
              data_f,  { 
                y: "year",  x: (d, i) => (i % 2 === 0 ? 6 : -6 ), 
                dy: -5,
                text: (d) => d.year.toString(),
                opacity: (d,i) => data_f[i > 0 ? i-1 : data_f.length-1].year === data_f[i].year ? 0 : 1
              }
            ),
            Plot.text(
              data_f, 
              {
                filter: (d, i) => (i % 2 === 0),
                y: d => d.year, 
                x: 25 , 
                text: d => `${d.title} (${d.short_title}${d.contrib_type})`, 
                textAnchor: "start",
                lineWidth: 28, 
                tip: true,
                title: d => `tldr; ${d.tldr}`
            }),
            Plot.text(
              data_f, 
              {
                filter: (d, i) => (i % 2 !== 0),
                y: d => d.year, 
                x: -25 , 
                text: d => `${d.title} (${d.short_title}${d.contrib_type})`, 
                textAnchor: "end",
                lineWidth: 24, 
                tip: true,
                title: d => `tldr; ${d.tldr}`
            }),
          ],
        })
    )}
    </div>
    <br>
    <div class="ridge">
    <small>${summaries[select]}</small>
    </div>
  </div>
  </center>
</div>

```js
data_f.map((d,i) => data_f[i > 0 ? i-1 : data_f.length-1].year === data_f[i].year)
```

```js
const summaries = {
  'pinned': 'todo 🚧',
  'CGS': 'todo 🚧',
  'φ': 'todo 🚧',
  'S': 'todo 🚧',
  'B': 'todo 🚧',
  'PS': html`<span class="highlight-purple">Collective action theory</span> is derived from Elinor Ostrom's views of social dilemmas, and is typically characterized by its used of public good games. Although it informed by the social sciences, we find that they state a disting set of questions that is important to the study of groups and unique to that literature. The key idea of that literature is how groups can self-govern themselves in the face of a social dilemmas, under particular conditions. Groups can evolve set of rules to prevent the tragedy of the commons, they are not as 'mindless' as once thought. That being said, this literature is often characterized by smaller groups, in which there is a sense of joint commitment toward the common-pool resources.`,
  'P': 'todo 🚧'
}
```

```js
const data_f = d3.sort(select === 'pinned' ? 
            data.filter(d => pinned_title.includes(d.short_title)) : 
            data.filter(d => d.subfield == select), (a,b) => d3.ascending(a.year, b.year))
```

## The social ontology of groups

<ul class="task-list">
  <li><input type="checkbox">Basic grouping that can be node- or edge-first based on shared property (no interactions; no intentionality)</li>
  <li><input type="checkbox">Intentional groups (reducible; adding mental states)</li>
    <li><input type="checkbox">Non-reducible intentional groups.</li>
</ul>

#### Back to the basics

We like to put marbles, books, or cards that share some quality or feature together. This shared property—color, size, and so—allows for ordering. We call this ordered collection a grouping, or cluster, and they sometime serve a functional goal, such as searching for a good hand in card games. Or it can be purely esthetics, such as organizing books based on color. Philosophers call this grouping 'natural kinds'. Similarly, one can cluster  based on relation of interest. For instance, Mars and Jupiter are similar in that they orbit the sun. Otherwise, they couldn't be more different as planet.

A well-known fact social psychology, is how Western Educated Industrialized Rich and Democratic (WEIRD) societies tend to put individuals, or entities, before interactions. When asked to introspect during the 'Who Am I?' test, psychologists found again and again that WEIRD people define themselves in terms of individual attributes (CITE). In many other cultures, such as Japan, they might define themselves with respect to their relationships, e.g. 'I am Sora's professor' instead of 'I am a teacher'. 

Similarly, we can think of how the [distributional hypothesis](https://en.wikipedia.org/wiki/Distributional_semantics) revolutionized our way to represent text in linguistics. That is, we went from representing text as bag-of-words, where the fundamental units are word counts, to representing text in a continous representations where word coordinates encode the _context_ in which we find the words. This shift allowed us to have a less WEIRD representation of text where from coordinates alone, we could extract semantic relationships, e.g. 'the hammer is to the nail as the screwdriver is to the screw'.

We can build networks out of these interactions because we now have a notion of nodes and edges. Until recently, researchers in network science did not realize how useful it is to adopt edge-first view; clustering on links lead naturally to the idea of hierarchy (groups part of groups) and overlapping communities (I am both a teacher and a father) (CITE Bagrow ?). [EXPLAIN].

#### Intentional groups

The components involved in interactions may or may not involve intentionality. Intentional agents possess mental states. The same grouping can be interepreted with or without intentionality. For example, a group of sperm whales can be classified based on shared features without considering whether they are intentional agents. They are groups by virtue of sharing some features, such as feeding and migration behaviors, size, or communicating via echolocation and vocalization. 

However, recent studies have shown that sperm whales have a matrilineally based social organization, meaning that males tend to leave the clans while female offsprings stay with their moms (CITE whitehead). Moreover, groups who are tightly knit might develop accent when vocalizing, distinguishing between in groups and out groups. When groups depend on intentionality and a share identity, there is a sense where individuals have mental states that can tell whether they are part of the group or not. The young males "believe" they are not part of their mothers' group when they come to age, not unlike how traditional matrilineal societies work in humans. 

<div class="note">In sociology and anthropology, an important distinction is made between primary groups, which is characterized by intimate, lifelong relationships (think of kins, close friends, romantic partners), and secondary groups, which are characterized by goal-oriented and more temporary relationships. In network science, we would associate secondary groups with long ties, which can be essential to shorter longest paths in a social network.</div>

<div class="note">Well known methods in social science using networks to study groups: stochastic actor oriented models (SOAM; Snijders 2010), exponential random graph models (ERGM)</div>

#### Non-reducible, intentional groups

A group becomes irreducible to its constituents when group membership is conditional on each other's beliefs.

<!-- #### Intentionality and unit of adaptation

<ul class="task-list">
  <li><input type="checkbox">How does group as unit of adaptation is connected to non-reducible groups</li>
</ul>

Non-reducibility is at the heart of the original debate on the evolution of groups in biology in the 1960s. Wynne-Edwards put forth the idea that groups could be a unit of adaption. That some behaviors could serve for the benefit of the groups such as individual reulating  -->

## The social science and its relationship to evolutionary science


<ul class="task-list">
  <li><input type="checkbox">Sociologists inheriting from Simmel vs evolutionary thinkers</li>
</ul>

Textbook definition in sociology, cultural anthropology or social psychology of groups might include different perspectives, types of social groups, and recurrent notions deemed important to the study of groups: 
 - [functionalist, critical, feminist, symbolic interactionist](https://opentextbc.ca/introductiontosociology/chapter/chapter6-groups-and-organization/)
 - notions of in- and out-groups
 - group leadership
 - group size
 - norms and formal organizations: at some points groups, adopt norms and rules that make it less fun for the original members. This is often where we shift from social groups to voluntary organizations and institutions.
 - Specialization: some people have specific roles in the groups, which can be formal or not.


## Pragmatic approach to the studies of groups

<ul class="task-list">
  <li><input type="checkbox">What is the grontology pragmatic approach</li>
  <li><input type="checkbox">Why do we care?</li>
</ul>

Policy studies can be characterize in terms of tragedy of the commons, governance and the coevolution of institutional policies and group organization, as well as bringing game-theoric notions to the discussion (CITE OSTROM).


## Additional references

 - [Stanford Encyclopedia of Philosophy's entry on Social Ontology (§ Social Groups)](https://plato.stanford.edu/entries/social-ontology/#KeyDomaAddrSociOnto): Great introduction to the philosophical enterprise that is the study of social ontology; what it is and why do we care. 


```js
const fos2cat = {
"pinned": "Sacred timeline", "S":"Classical social sciences", "B":"Biological group selection", "φ": "Philosophy", "CGS": "Cultural group selection", "P": "HONs", "PS": "Collective action theory"}

const pinned_title = ['campbell_common_1958', 'wynne-edwards_animal_1962', 'neal_duality_2023',   'smith_group_1976', 'okasha_why_2001', 'sterelny_return_1996', 'breiger_duality_1974', 'boyd_culture_1985' , 'ostrom_covenants_1992', 'gilbert_rationality_2006', 'smaldino_cultural_2014' ,'french_collective_1984', 'battiston_physics_2021']
```

```js
const data = FileAttachment("data/lit_review.csv").csv({typed: true});
```

<!-- STYLE CSS -->


<style type="text/css">
  div.ridge {
    border-style: groove;
    border-width: 1px;
    padding: 20px;
    width: 75%;
    margin-left: 20px;
  }

  .highlight-red {
      color:  #dc143c;          /* Change the color to red */
      text-decoration: underline; /* Underline the text */
  }
  .highlight-blue {
      color: #1e90ff;          /* Change the color to red */
      text-decoration: underline; /* Underline the text */
  }
  .highlight-green {
      color: #32cd32;          /* Change the color to red */
      text-decoration: underline; /* Underline the text */
  }
  .highlight-purple {
      color: #9370db;          /* Change the color to red */
      text-decoration: underline; /* Underline the text */
  }
  .highlight-coral {
      color: #ff7f50;          /* Change the color to red */
      text-decoration: underline; /* Underline the text */
  }

.focus {
  color: var(--theme-foreground-focus);
  border-radius: 8px;
  margin: 1rem;
  box-shadow: 0 0 0 0.75px rgba(128, 128, 128, 0.2), 0 6px 12px 6px rgba(0, 0, 0, 0.4);
}

.invert {
  background-color: var(--theme-foreground-alt);
  color: var(--theme-background);
}

.crop {
  border-radius: 8px;
  margin: 1rem;
  max-width: calc(50% - 2rem);
  box-shadow: 0 0 0 0.75px rgba(128, 128, 128, 0.2), 0 6px 12px 6px rgba(0, 0, 0, 0.4);
  aspect-ratio: 3024 / 1888;
  object-fit: cover;
  object-position: 0 100%;
}

.wbr::before {
  content: "\200b";
}

.wide {
  max-width: 960px;
}

figcaption code {
  font-size: 90%; /* TODO move to global.css */
}

@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');

 ul {
        list-style-type: disc;
        padding-left: 20px;
    }

/* Style for the task list */
    .task-list {
        list-style-type: none;
        padding: 0;
    }

 .task-list li {
        margin-bottom: 10px;
        padding: 5px 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

/* Style for the checkbox */
     .task-list input[type="checkbox"] {
        margin-right: 10px;
    }
</style>


```js
data_f
```