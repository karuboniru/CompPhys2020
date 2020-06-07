#include "TCanvas.h"
#include "TROOT.h"
#include "TGraphErrors.h"
#include "TF1.h"
#include "TLegend.h"
#include "TArrow.h"
#include "TLatex.h"
#include <vector>

void macro4()
{
    std::vector<double> x_vals =
        {0.01,
         0.00909090909090909,
         0.008333333333333333,
         0.007692307692307693,
         0.007142857142857143,
         0.006666666666666667,
         0.00625,
         0.0058823529411764705,
         0.005555555555555556,
         0.005263157894736842,
         0.005};
    std::vector<double> y_vals =
        {-30.011614979335214,
         -32.70796978910237,
         -35.05522463350979,
         -38.46913154114128,
         -41.479329103212265,
         -44.402718232352115,
         -47.39207291940111,
         -51.748989796125144,
         -53.70699692413216,
         -55.60232475091072,
         -59.994207324767366};
    std::vector<double> y_errs =
        {4.377615414166447,
         4.386592517748182,
         4.346964728338778,
         5.333065837952921,
         5.198978173235851,
         5.095095373468879,
         5.383790131965032,
         6.016731337757642,
         5.793842119855691,
         5.85572726588655,
         6.282257848206238};

    // Instance of the graph
    TGraphErrors graph(x_vals.size(), &x_vals[0], &y_vals[0], nullptr, &y_errs[0]);
    graph.SetTitle("; 1/N; Total Energy");
    // Make the plot estetically better
    graph.SetMarkerStyle(kOpenCircle);
    graph.SetMarkerColor(kBlue);
    graph.SetLineColor(kBlue);
    auto func = new TF1("func", "[0]*TMath::Power(x, [1])", 0, 1);
    func->SetParameter(0, -10);
    func->SetParameter(1, -0.5);
    graph.Fit(func);
    // The canvas on which we'll draw the graph
    auto mycanvas = new TCanvas();
    auto leg = new TLegend(.1, .7, .3, .9);
    leg->AddEntry(&graph, "Results");
    leg->AddEntry(func, "Fit");
    // mycanvas->SetLogy();
    // mycanvas->SetLogx();
    // Draw the graph !
    graph.DrawClone("APEL");
    leg->DrawClone("Same");

    mycanvas->Print("fit_exp2_h.eps");
}
