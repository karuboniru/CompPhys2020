#include "TCanvas.h"
#include "TROOT.h"
#include "TGraphErrors.h"
#include "TF1.h"
#include "TLegend.h"
#include "TArrow.h"
#include "TLatex.h"
#include <vector>

void macro2()
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
        {-162.84772540691984,
         -180.47414030051675,
         -194.6905836031798,
         -226.98466362889522,
         -208.0384688380757,
         -234.48248465534485,
         -263.6949232187414,
         -268.5008396651098,
         -258.463942373997,
         -305.26825233098555,
         -299.18398183008145};
    std::vector<double> y_errs =
        {8.182537060319708,
         7.81001350868659,
         6.1180051612648985,
         6.033680014432955,
         13.808175000872934,
         5.703734566402483,
         11.531100865060758,
         15.705522390737194,
         23.11923046573023,
         13.204365624094782,
         16.551958551655485};

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

    mycanvas->Print("fit_exp1_h.eps");
}
