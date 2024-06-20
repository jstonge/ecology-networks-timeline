
<div>
    <center>
    <h4>Multiverse literature review (WIP)</h4>
    <br>
    <div>${resize((width) => 
      Plot.plot({
          width,
          height: 900,
          marginBottom: 50, 
          marginTop: 50, 
          marginLeft:20,
          y: { axis: null, reverse: true, insetTop: 20 },
          facet: {data: data_f, x: "source"},
          fx: {padding: 0.05, label: null},
          x: { axis: null, domain: [-200 / 2, 200 / 2] },
          marks: [
            Plot.axisFx({anchor: "top"}),
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
                lineWidth: 20, 
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
                lineWidth: 20, 
                tip: true,
                title: d => `tldr; ${d.tldr}`
            }),
          ],
        })
    )}
    </div>
    <br>
    <div class="ridge">
    </div>
  </div>
  </center>
</div>



```js
const data_f = d3.sort(data, (a,b) => d3.ascending(a.year, b.year))
```

```js

data_f
```


```js
const fos2cat = {"E":"Community Ecology", "D": "Structure and Dynamics", "S": "Spatial"}
```

```js
const data = FileAttachment("data/lit_review.csv").csv({typed: true});
```