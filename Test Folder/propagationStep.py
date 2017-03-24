
function propagationStep (lgraph, rgraph, mapping)
    scores[lnode] = matchScores(lgraph, rgraph, mapping, lnode)
    if eccentricity(scores[lnode])<theta: continue
    rnode = (pick node from right.nodes where scores[lnode][node]=max(scores[lnode]))

    scores[rnode]=matchScores(rgraph, lgraph, invert(mapping),rnode)
    if eccentricity(scores[rnode]=max(scores[rnode]))
    reverse_match = (pick node from lgraph.nodes where scores[rnode][node]=max(scores[rnode]))

    if reverse_match != rnode:
        continue

    mapping[lnode]=rnode

function matchScores(lgraph, rgraph, mapping, lnode)

function eccentricity(items)
    return ((max(items)-max2(items))/std_dev(items))

until convergence do:
    propagationStep(lgraph, rgraph, seed_mapping)
