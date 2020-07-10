// REF:  http://js.cytoscape.org/#core
//
// Assumes cy variables has already been loaded.


/***************************************
 * STYLE OPTIONS
 * https://js.cytoscape.org/#cy.style
 * 
/**************************************/

cy.style()
    .selector('node')
      .style({
        "label": "data(label)",
        "text-valign": "center",
        "text-halign": "right",
        "text-margin-x": -155,
        "text-wrap": "wrap",
        "text-max-width": 150,
        "background-position-x": 0,
        "height": 24,
        "font-size": 12,
        "background-fit": "contain",
        "shape": "roundrectangle",
        "background-opacity": 0,
        "width": 180,
        "border-width": 1,
        "padding-right": 5,
        "padding-left": 5,
        "padding-top": 5,
        "padding-bottom": 5,
        "text-events": "yes",
        "background": "data(background)",
      })
    .selector("edge")
      .style({
        "width": 1,
        "curve-style": "bezier",
        // "curve-style": "taxi",
        "taxi-direction": "vertical",
        "taxi-turn": "15px",
        "taxi-turn-min-distance": "15px",
        "line-color": "black",
        "line-style": "solid",
        "target-arrow-shape": "triangle-backcurve",
        "target-arrow-color": "black",
      })
    .selector("edge[label]") // add labels to edges that have them.
      .style({
        "text-rotation": "0deg",
        "label": "data(label)",
        "text-halign": "right",
        // "text-max-width": 130,
        // "text-min-width": 130,
      })
    .selector("$node > node") // compound nodes (campaigns)
      .style({
        "text-rotation": "-90deg",
        "text-halign": "left",
        "text-margin-x": -10,
        "text-margin-y": -40
      })
    .selector('.repeat-edge')
      .style({
        'loop-direction': '100deg', 
        'loop-sweep': '-20deg',
        'target-endpoint': '90deg',
        'source-endpoint': '103deg',
        'control-point-step-size': 80,
        'text-margin-x': 10,
        'text-margin-y': -3,
        'font-size': 12,
      })
    .selector('.alternate-edge')
      .style({
        "line-style": "dashed",
      })
    .selector(".link_hover")
      .style({
        "background-opacity": 1,
        "background-color": "#e5e5e5"
      })
    .selector(".link")
      .style({
        "color": "#2f70a8",
        "border-color": "#2f70a8"
      })
    .selector (".Badge")
      .style({
        "border-width": 3,
        "shape": "cut-rectangle",
      })
    .selector(".hidden")
      .style({
        "opacity": 0
      })
    .update()
;


/***************************************
 * LAYOUT OPTIONS
 * https://js.cytoscape.org/#core/layout
 * 
/**************************************/

var layout = cy.layout({

    // name: 'breadthfirst',
    // directed: true,
    // grid: false,
    // spacingFactor: 0.5,
    // maximal: true,
    animate: true,
    "name": "dagre",
    "nodeSep": 60,  // horizontal seperation of campaigns/chains/columns
    "rankSep": 24  // vertical seperation of nodes
});
layout.run();

/***************************************
 * 
 * BEHAVIOUR/INTERACTIVE OPTIONS
 * 
/**************************************/

// redirect to link
cy.on('tap', '[href]', function(){
    window.location.href = this.data('href');
});

cy.on('mouseover', '[href]', function(){
    $('#cy').css('cursor', 'pointer');
    this.addClass('link_hover');
});
cy.on('mouseout', '[href]', function(){
    $('#cy').css('cursor', 'move');
    this.removeClass('link_hover');
});

// nodes that don't link
cy.on('mouseover', '[^href]', function(){
    $('#cy').css('cursor', 'default');
});
cy.on('mouseout', '[^href]', function(){
    $('#cy').css('cursor', 'move');
});


cy.on('ready', function () {
    updateBounds();
});


$(document).ready(function() { 
    updateBounds();
    //if they resize the window, resize the diagram
    $(window).resize(function () {
        updateBounds();
    });
    cy.center();
    cy.resize();

}); // dom ready

var updateBounds = function () {
    var bounds = cy.elements().boundingBox();
    $('#cy').css('height', bounds.h + 50);
    cy.center();
    cy.resize();
};

$("#btn-fullscreen").click(function() {
    $("#cy").toggleClass("fullscreen");
    $("#fullscreen").toggleClass("fullscreen-toggle");
})

$("#btn-print").click(function() {
    var png64 = cy.png({
        full: true
    });
    var windowContent = '<!DOCTYPE html>';
    windowContent += '<html>'
    windowContent += '<head><title>Print canvas</title></head>';
    windowContent += '<body>'
    windowContent += '<img src="' + png64 + '">';
    windowContent += '</body>';
    windowContent += '</html>';
    var printWin = window.open();
    printWin.document.open();
    printWin.document.write(windowContent);
    printWin.document.close();
    printWin.focus();
    printWin.print();
});
