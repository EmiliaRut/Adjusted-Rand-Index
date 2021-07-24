from cdlib import evaluation, NodeClustering, readwrite

file1 = "Input/June2_adj_90&15_40_1_SumAbs_Paper2.csv"
file2 = "Input/June2_orig_90&15_40_1_SumAbs_Paper2.csv"
output_file = open('Output/'+file1.replace("Input/", "").replace(".csv", "")+'_vs_'+file2.replace("Input/", "").replace(".csv", "")+'.txt', 'w')

community_one = readwrite.read_community_csv(file1, ",", str)
community_two = readwrite.read_community_csv(file2, ",", str)

coms_one = NodeClustering(community_one, graph=None, method_name="your_method")
coms_two = NodeClustering(community_two, graph=None, method_name="your_method")

print(evaluation.adjusted_rand_index(coms_one, coms_two), file=output_file)

# readwrite.write_community_csv(community_one, "Output/write_community_test.csv", ",")