#include "TCanvas.h"
#include "TROOT.h"
#include "TGraphErrors.h"
#include "TF1.h"
#include "TLegend.h"
#include "TArrow.h"
#include "TLatex.h"
#include <vector>

void macro3()
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
        {-30.77555834338995,
         -33.63399148616336,
         -35.908753242475996,
         -39.169980774424914,
         -42.26417044045025,
         -45.92378400610906,
         -49.21706000345957,
         -52.10187988130799,
         -55.115088187270864,
         -57.71037126154101,
         -62.078372341991816};
    std::vector<double> y_errs =
        {4.238310539441237,
         4.512345042389744,
         5.0283580600715,
         4.449936341300379,
         4.650917507845609,
         5.378140638052913,
         5.595217447580532,
         5.479949519189961,
         6.1228883762015975,
         5.927788641713097,
         6.102235394424728};

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

    mycanvas->Print("fit_exp2.eps");
}
