#include "TCanvas.h"
#include "TROOT.h"
#include "TGraphErrors.h"
#include "TF1.h"
#include "TLegend.h"
#include "TArrow.h"
#include "TLatex.h"
#include <vector>

void macro4_f()
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
        {19.16351671, 19.24219392, 18.89610235, 28.44159123, 27.02937405,
         25.95999686, 28.98519619, 36.20105599, 33.56860651, 34.28954181,
         39.46676367};

    // Instance of the graph
    TGraphErrors graph(x_vals.size(), &x_vals[0], &y_vals[0], nullptr, nullptr);
    graph.SetTitle("; 1/N; Fluctuation");
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
    auto leg = new TLegend(.7, .7, .9, .9);
    leg->AddEntry(&graph, "Results");
    leg->AddEntry(func, "Fit");
    // mycanvas->SetLogy();
    // mycanvas->SetLogx();
    // Draw the graph !
    graph.DrawClone("APEL");
    leg->DrawClone("Same");

    mycanvas->Print("fit_exp2_f_h.eps");
}
