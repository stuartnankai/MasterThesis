
###################################

library(pheatmap)
library(rworldmap)
library(stringi)
library(spaa)
library(ape)
library(phytools)

### Give files ###

readfile <- "~/aquatic/baltic_winter/otus/data_All_2016_otus.txt"
envfile <- "~/aquatic/baltic_winter/info/data_All_2016_metadata.txt"
treefile <- "~/aquatic/baltic_winter/phylodist/tree_Daniel.ntree"

#### Read data ####################

# you will have to change the column numbers here since the file format Daniel has generated is probably not the same as mine used to be!

tab <- read.delim(readfile)
id <- tab[,1]
taxonomy <- as.matrix(tab[,2])
reads <- as.matrix(tab[,3:ncol(tab)]) # reads is a matrix with all otu counts (and nothing else), samples in same order as in input file
sample <- colnames(reads)

# make a normalized version of reads, i.e. divide each count by sample total
norm_reads <- reads
for (i in 1:ncol(reads)) {
	norm_reads[,i] <- reads[,i]/sum(reads[,i])
}

binary_reads <- reads
binary_reads[which(reads > 0)] = 1

winter_sample <- sample[grep("W", sample)]
summer_sample <- sample[grep("S", sample)]
norm_reads <- norm_reads[, match(c(winter_sample, summer_sample), sample)]
reads <- reads[, match(c(winter_sample, summer_sample), sample)]
sample <- c(winter_sample, summer_sample)
winter_sample <- sample[grep("W", sample)]
summer_sample <- sample[grep("S", sample)]
colnames(reads) = sample
colnames(norm_reads) = sample

# make clade count tables

a<-strsplit(taxonomy,";")
res<-as.data.frame(t(stri_list2matrix(a)))
colnames(res)<-c("Domain","Phylum","Class","Order","Family","Genus")
clade_reads = list()
clade_norm_reads = list()
for (i in 1:ncol(res)) {
  matr = NULL
  clade = c()
  for (j in 1:nlevels(res[,i])) {
    if (levels(res[,i])[j]!="Unclassified") {
      if (levels(res[,i])[j]!="unclassified") {
        if (levels(res[,i])[j]!="Uncultured") {
          if (levels(res[,i])[j]!="uncultured") {
            ix = which(levels(res[,i])[j]==res[,i])
            clade = c(clade, levels(res[,i])[j])
            if (length(ix) > 1) {
              matr = rbind(matr, apply(reads[ix,], 2, sum))
            } else {
              matr = rbind(matr, reads[ix,])
            }
          }
        }
      }
    }
  }
  rownames(matr) = clade
  colnames(matr) = sample
  clade_norm_reads[[i]] = clade_reads[[i]] = matr
  for (j in 1:nrow(matr)) { clade_norm_reads[[i]][j,] = matr[j,]/apply(reads, 2, sum) }
}

#### Read env data ################

env <- read.delim(envfile, row.names = 1)
env <- as.matrix(env)
env <- env[match(sample, rownames(env)) ,]

#Station <- env[,4]
#Date <- env[,7]
#Time <- env[,8]
Temp <- as.numeric(env[,3])
Depth <- as.numeric(env[,2])
PO4 <-  as.numeric(env[,5])
SIO2 <- as.numeric(env[,6])
NH4 <- as.numeric(env[,9])
NO2 <- as.numeric(env[,7])
NO3 <- as.numeric(env[,8])
O2 <- as.numeric(env[,4])
Sal <- as.numeric(env[,1])
Lat <- as.numeric(env[,13])
Lon <- as.numeric(env[,14])
Sal_cat <- env[,16]

Is_summer <- c( rep(0, length(winter_sample)), rep(1, length(summer_sample)) ) 
Season <- c( rep(1, length(winter_sample)), rep(2, length(summer_sample)) ) # 1 for winter, 2 for summer

env <- rbind(Depth, Lat, Lon, Temp, Sal, NO2, NO3, PO4, SIO2, O2, Season)

#### Making sample groups ####

g_all <- c(1:length(sample))
g_winter <- grep("W", sample)
g_summer <- grep("S", sample)
g_surface <- which(Depth <= 10)
g_summer_surface <- intersect(g_summer, g_surface)
g_winter_surface <- intersect(g_winter, g_surface)

plot(Lon[g_summer], Lat[g_summer], pch = 1, cex = 3, col = "darkred")
points(Lon[g_winter], Lat[g_winter], pch = 1, cex = 2, col = "blue")

joint <- c( # these are all surface samples, one sample per season and location
  "S1",
  "S107",
  "S111",
  "S15",
  "S19",
  "S207",
  "S216",
  "S226",
  "S27",
  "S3",
  "S31",
  "S39",
  "S67",
  "S71",
  #"S72",
  "S75",
  "S9",
  "S96",
  "W021",
  "W031",
  "W035",
  "W047",
  "W052",
  "W061",
  "W067",
  "W089",
  "W093",
  "W096",
  "W102",
  "W145",
  "W155",
  "W159",
  "W167",
  "W182",
  #"W185",
  "W188")

g_joint = match(joint, sample)

g_joint_summer = intersect(g_joint, g_summer)
g_joint_winter = intersect(g_joint, g_winter)

plot(Lon[g_joint_summer], Lat[g_joint_summer], pch = 1, cex = 3, col = "darkred")
points(Lon[g_joint_winter], Lat[g_joint_winter], pch = 1, cex = 2, col = "blue")

#shared_stations <- intersect(Station[g_winter], Station[g_summer])
#shared_stations <- shared_stations[which(!is.na(shared_stations))]
#g_shared_stations <- c()
#for (i in 1:length(shared_stations)) {
#	g_shared_stations <- c(g_shared_stations, grep(shared_stations[i], Station))
#}
#shared_surface_stations <- intersect(Station[g_winter_surface], Station[g_summer_surface])
#shared_surface_stations <- shared_surface_stations[which(!is.na(shared_surface_stations))]
#g_shared_surface_stations <- c( # One summer and one winter surface sample selected per station
#g_winter_surface[match(shared_surface_stations, Station[g_winter_surface])],
#g_summer_surface[match(shared_surface_stations, Station[g_summer_surface])]
#)
#plot(Lon[intersect(g_summer, g_shared_stations)], Lat[intersect(g_summer, g_shared_stations)], pch = 1, cex = 3, col = "darkred")
#points(Lon[intersect(g_winter, g_shared_stations)], Lat[intersect(g_winter, g_shared_stations)], pch = 1, cex = 2, col = "blue")
#
#plot(Lon[intersect(g_winter, g_shared_stations)], Lat[intersect(g_winter, g_shared_stations)], pch = 1, cex = 2, col = "lightgrey", xlim = c(8,24))
#text(Lon[intersect(g_winter, g_shared_stations)], Lat[intersect(g_winter, g_shared_stations)], Station[intersect(g_winter, g_shared_stations)])

# routes:

# west of Gotland (north -southwest)
tr_west_stations <- c(
"MM8-3036",
"MM8-3035",
"MM8-3034",
"MM8-3052",
"MM8-3054",
#"MM8-3055",
"MM8-3056",
"MM8-3057",
"MM8-3058",
"MM8-3059",
"MM8-3060",
"MM8-3061",
"MM8-3062",
"MM8-3006",
"MM8-3063",
"MM8-3064",
"MM8-3065",
"MM8-3003",
"MM8-3066",
"MM8-3001",
"MM8-3083",
"MM8-3082",
"MM8-3081",
"MM8-3080",
"MM8-3079",
"MM8-3075",
"MM8-3101",
"MM8-3102")

g_summer_tr_west_surface <- c(1)
for (i in 1:length(tr_west_stations)) {
	Depth[ intersect( grep(tr_west_stations[i], Station), g_summer ) ]
	ix <- sort(Depth[ intersect( grep(tr_west_stations[i], Station), g_summer ) ], index.return = TRUE, decreasing = FALSE)$ix[1]
	g_summer_tr_west_surface[i] <- intersect( grep(tr_west_stations[i], Station), g_summer )[ix]
}

g_winter_tr_west_surface <- c(1)
for (i in 1:length(tr_west_stations)) {
	Depth[ intersect( grep(tr_west_stations[i], Station), g_winter ) ]
	ix <- sort(Depth[ intersect( grep(tr_west_stations[i], Station), g_winter ) ], index.return = TRUE, decreasing = FALSE)$ix[1]
	g_winter_tr_west_surface[i] <- intersect( grep(tr_west_stations[i], Station), g_winter )[ix]
}

plot(Lon, Lat, col = "white")
points(Lon[g_summer], Lat[g_summer], col = "red", cex = 2)
points(Lon[g_winter], Lat[g_winter], col = "blue", cex = 3)
points(Lon[g_shared_stations], Lat[g_shared_stations], col = "black", cex = 1, pch = 20)
points(Lon[g_winter_tr_west_surface], Lat[g_winter_tr_west_surface], col = "darkgreen", cex = 4)
points(Lon[g_surface_shared_stations], Lat[g_surface_shared_stations], col = "brown", cex = 5)

#### colors and shapes and sizes #####

color_sal = colorRampPalette(rev(c("#D73027", "#FC8D59", "#FEE090", "#FFFFBF", "#E0F3F8", "#91BFDB", "#4575B4")))(max(Sal))
size_depth = log10(Depth) + 1
pch_season1 = rep(16, length(sample))
pch_season1[g_winter] = 17
pch_season2 = rep(1, length(sample))
pch_season2[g_winter] = 2

##### Calculate Shannon diversity (alpha-diversity) ######

shannon <- c(1)
for (i in 1:ncol(norm_reads)) {
	sum <- 0
	for (j in 1:nrow(norm_reads)) {
		if (norm_reads[j,i] > 0) {
			sum <- sum + ( log(norm_reads[j,i]) * norm_reads[j,i] )			
		}
	}
	shannon[i] <- -1 * sum 	
}

#### shannon vs sal ####

plot(Sal[which(Depth < 11)], shannon[which(Depth < 11)], cex = size[which(Depth < 11)]/1000)
text(Sal[which(Depth < 11)], shannon[which(Depth < 11)], sample[which(Depth < 11)], col = "red")

plot(Lon[which(Depth < 5)], Lat[which(Depth < 5)], cex = Sal[which(Depth < 5)]/3)
plot(Lon[which(Depth < 5)], Lat[which(Depth < 5)], cex = shannon[which(Depth < 5)])

boxplot(shannon[g_winter], shannon[g_summer])

#### Calc pair-wise sample distances (beta-diversity) ###

# This is done here with two approaches: 
# 1) by spearman correlations between pairs (this works good for environmental gradients)
# 2) by Bray-Curtis. A popular measurement in ecology
#
# One matrix is generated for each index. 
# In these samples are ordered in the same order as in reads, broth row and column wise, 
# and each cell is a pairwise community distance (between 0 and 1) 

library(vegan) # for bray curtis index

spearman_matr <- matrix(ncol = ncol(reads), nrow = ncol(reads))
for (i in 1:ncol(reads)) {
	for (j in 1:ncol(reads)) {
		ok <- which(reads[,i] + reads[,j] > 0)
		spearman_matr[i,j] = cor.test(reads[ok,i], reads[ok,j], method = "spearman")$est
	}
}
spearman_matr <- (-1*spearman_matr + 1) / 2

bray_matr <- as.matrix(vegdist(t(norm_reads), method="bray", binary=FALSE, diag=TRUE, upper=TRUE, na.rm = FALSE)) 

clade_spearman_matr = list()
for (i in 1:ncol(res)) {
  matr = matrix(ncol = ncol(reads), nrow = ncol(reads))
  rownames(matr) = colnames(matr) = sample
  for (j in 1:ncol(clade_reads[[i]])) {
    for (k in 1:ncol(clade_reads[[i]])) {
      ok <- which((clade_reads[[i]][,j] + clade_reads[[i]][,k]) > 0)
      if (length(ok) > 1) {
        matr[j,k] = cor.test(clade_reads[[i]][ok,j], clade_reads[[i]][ok,k], method = "spearman")$est
      }
    }
  }
  matr <- (-1*matr + 1) / 2
  clade_spearman_matr[[i]] = matr
}
clade_spearman_matr[[7]] = spearman_matr

clade_bray_matr = list()
for (i in 1:ncol(res)) {
  matr =as.matrix(vegdist(t(clade_norm_reads[[i]]), method="bray", binary=FALSE, diag=TRUE, upper=TRUE, na.rm = FALSE))
  rownames(matr) = colnames(matr) = sample
  clade_bray_matr[[i]] = matr
}
clade_bray_matr[[7]] = bray_matr


##########################################################
#### Calc pair-wise sample distances based on Env data ###

saldiff_matr <- matrix(ncol = ncol(reads), nrow = ncol(reads))
for (i in 1:ncol(reads)) {
  for (j in 1:ncol(reads)) {
    saldiff_matr[i,j] = abs(Sal[i] - Sal[j])
  } 
}

tempdiff_matr <- matrix(ncol = ncol(reads), nrow = ncol(reads))
for (i in 1:ncol(reads)) {
  for (j in 1:ncol(reads)) {
    tempdiff_matr[i,j] = abs(Temp[i] - Temp[j])
  } 
}

rownames(saldiff_matr) = colnames(saldiff_matr) = sample
rownames(tempdiff_matr) = colnames(tempdiff_matr) = sample

######################################
############ PCOA and NMDS ###########

#these <- 1:length(sample)
#these <- g_surface
these <- g_joint
size = size_depth[these]
pch1 = pch_season1[these]
pch2 = pch_season2[these]
color = color_sal[ Sal[these] ]

#nmds
names = c("Phylum", "Class", "Order",  "Family", "Genus", "OTU")
par(mfrow=c(3,2), mar=c(4,4,1,1))
for (i in 2:7) {
  #dist_matr = clade_spearman_matr[[i]][these,these]
  dist_matr = clade_bray_matr[[i]][these,these]
  mds <- metaMDS(dist_matr)
  plot(mds$points[,1], mds$points[,2], cex = size, pch = pch1, col = color, xlab = "NMDS1", ylab = "NMDS2")
  points(mds$points[,1], mds$points[,2], cex = size, pch = pch2, col = "black")
  legend("bottomright",c("Winter","Summer"),pch=c(17,16),inset=0.01,lty=c(0,0),cex=1,bg="white", col=c("black", "black"))
  legend("topleft",names[i-1],inset=0.01,bty="n",cex=1.5,bg="white", col=c("black"))
}

#pcoa
names = c("Phylum", "Class", "Order",  "Family", "Genus", "OTU")
par(mfrow=c(3,2), mar=c(4,4,1,1))
for (i in 2:7) {
  #dist_matr = clade_spearman_matr[[i]][these,these]
  dist_matr = clade_bray_matr[[i]][these,these]
  pcoa <- pcoa(dist_matr, correction = "cailliez")
  xlab = paste("PC1 (", 100*round(pcoa$values[1,3], 2), "%)", sep = "")
  ylab = paste("PC2 (", 100*round(pcoa$values[2,3], 2), "%)", sep = "")
  plot(pcoa$vectors[,1], pcoa$vectors[,2], cex = size, pch = pch1, col = color, xlab = xlab, ylab = ylab)
  points(pcoa$vectors[,1], pcoa$vectors[,2], cex = size, pch = pch2, col = "black")
  legend("bottomright",c("Winter","Summer"),pch=c(17,16),inset=0.01,lty=c(0,0),cex=1,bg="white", col=c("black", "black"))
  legend("topleft",names[i-1],inset=0.01,bty="n",cex=1.5,bg="white", col=c("black"))
}


mds <- metaMDS(dist_matr)
pcoa <- pcoa(dist_matr, correction = "cailliez")
barplot(pcoa$values[1:10,3])

cor.test(pcoa$vectors[,1], Sal[these], method = "spearman")
plot(pcoa$vectors[,1], Sal[these])
plot(pcoa$vectors[,1], Temp[these])

par(mfrow=c(3,3), mar=c(4,4,1,1))
newmap <- getMap(resolution = "low")
plot(newmap, xlim = c(8, 25), ylim = c(56, 65), asp = 1)
points(Lon[these], Lat[these], cex = 4*(size+4)/max(size), pch = 16, col = color)
points(Lon[these], Lat[these], cex = 4*(size+4)/max(size), pch = 1, col = "black")

par(mfrow=c(2,2), mar=c(4,4,1,1))
# pcao
xlab = paste("PC1 (", 100*round(pcoa$values[1,3], 2), "%)", sep = "")
ylab = paste("PC2 (", 100*round(pcoa$values[2,3], 2), "%)", sep = "")
plot(pcoa$vectors[,1], pcoa$vectors[,2], cex = size, pch = pch1, col = color, xlab = xlab, ylab = ylab)
points(pcoa$vectors[,1], pcoa$vectors[,2], cex = size, pch = pch2, col = "black")
plot(Sal[these], pcoa$vectors[,1], cex = size, pch = pch1, col = color, xlab = "Salinity", ylab = "PC1")
points(Sal[these], pcoa$vectors[,1], cex = size, pch = pch2, col = "black")
# mds
plot(mds$points[,1], mds$points[,2], cex = size, pch = pch1, col = color, xlab = "NMDS1", ylab = "NMDS2")
points(mds$points[,1], mds$points[,2], cex = size, pch = pch2, col = "black")
plot(Sal[these], mds$points[,1], cex = size, pch = pch1, col = color, xlab = "Salinity", ylab = "NMDS1")
points(Sal[these], mds$points[,1], cex = size, pch = pch2, col = "black")

par(mfrow=c(2,2), mar=c(4,4,1,1))
# pcao
plot(pcoa$vectors[,1], pcoa$vectors[,2], cex = size, pch = pch1, col = color, xlab = xlab, ylab = ylab)
points(pcoa$vectors[,1], pcoa$vectors[,2], cex = size, pch = pch2, col = "black")

par(mfrow=c(2,2), mar=c(4,4,1,1))
plot(mds$points[,1], mds$points[,2], cex = size, pch = pch1, col = color, xlab = "NMDS1", ylab = "NMDS2")
points(mds$points[,1], mds$points[,2], cex = size, pch = pch2, col = "black")
plot(Sal[these], mds$points[,1], cex = size, pch = pch1, col = color, xlab = "Salinity", ylab = "NMDS1")
points(Sal[these], mds$points[,1], cex = size, pch = pch2, col = "black")

############
## ANOSIM ##

#these = 1:length(sample)
#these = g_surface
these = g_joint

grouping1 = Sal_cat
grouping2 = rep("summer", length(sample))
grouping2[grep("W", sample)] = "winter"
grouping1 = grouping1[these]
grouping2 = grouping2[these]

matr = matrix(ncol = 4, nrow = 6)
colnames(matr) = c("Sal-r", "Sal-p", "Season-r", "Season-p")
rownames(matr) = c("Phylum", "Class", "Order",  "Family", "Genus", "OTU")
for (i in 2:7) {
  #dist_matr = clade_spearman_matr[[i]][these,these]
  dist_matr = clade_bray_matr[[i]][these,these]
  anosim <- anosim(dist_matr, grouping1)
  matr[i-1,1] = anosim$statistic
  matr[i-1,2] = anosim$signif
  anosim <- anosim(dist_matr, grouping2)
  matr[i-1,3] = anosim$statistic
  matr[i-1,4] = anosim$signif
}
matr

# bray-curtis all samples:
Sal-r Sal-p  Season-r Season-p
Phylum 0.2597880 0.001 0.2326311    0.001
Class  0.3638634 0.001 0.2038665    0.001
Order  0.3403102 0.001 0.2843325    0.001
Family 0.3938382 0.001 0.2558506    0.001
Genus  0.4203822 0.001 0.2393804    0.001
OTU    0.4161708 0.001 0.2528509    0.001

# bray-curtis - surface samples:
Sal-r Sal-p  Season-r Season-p
Phylum 0.4581097 0.001 0.2450082    0.001
Class  0.6209781 0.001 0.2499792    0.001
Order  0.6354628 0.001 0.3411390    0.001
Family 0.6935497 0.001 0.3516124    0.001
Genus  0.7162157 0.001 0.3638947    0.001
OTU    0.6929740 0.001 0.4144749    0.001

# bray-curtis - g_joint samples:
Sal-r Sal-p  Season-r Season-p
Phylum 0.6017651 0.001 0.2807602    0.001
Class  0.7436261 0.001 0.2734582    0.001
Order  0.7384779 0.001 0.3230714    0.001
Family 0.7592885 0.001 0.3311368    0.001
Genus  0.8211212 0.001 0.3299919    0.001
OTU    0.8437023 0.001 0.4079483    0.001


# spearman all samples:
Sal-r Sal-p  Season-r Season-p
Phylum 0.2220848 0.001 0.2868644    0.001
Class  0.3184772 0.001 0.2375531    0.001
Order  0.3552116 0.001 0.2382680    0.001
Family 0.4220759 0.001 0.3372068    0.001
Genus  0.4295426 0.001 0.2850995    0.001
OTU    0.4531192 0.001 0.2569436    0.001

# spearman - surface samples:
Sal-r Sal-p  Season-r Season-p
Phylum 0.3199074 0.001 0.3448834    0.001
Class  0.4834786 0.001 0.3809997    0.001
Order  0.7163299 0.001 0.3191708    0.001
Family 0.7305579 0.001 0.4747031    0.001
Genus  0.6928010 0.001 0.4090986    0.001
OTU    0.7130794 0.001 0.3840307    0.001

# spearman - g_joint samples:
Sal-r Sal-p  Season-r Season-p
Phylum 0.4845282 0.001 0.1601109    0.002
Class  0.6550992 0.001 0.4085335    0.001
Order  0.7454238 0.001 0.3754071    0.001
Family 0.7583896 0.001 0.5146804    0.001
Genus  0.7684953 0.001 0.4576633    0.001
OTU    0.8305459 0.001 0.3953796    0.001



#### Do hierch. clustering of samples based on community distances ####

library(made4)
library(cluster)

# give vector of indices/samples to include
these <- c(1:length(sample)) # in this case all samples

# chose distance matrix to use
dist_matr <- spearman_matr[these,these]
#dist_matr <- bray_matr[these,these]
#dist_matr <- sorensen_matr[these,these]

# if you for instance want to put some env parameter as rownames (here salinity)
rownames(dist_matr) <- sample[these]
colnames(dist_matr) <- sample[these]

# make input format to agnes
j <- 2
distvec <- dist_matr[j:nrow(dist_matr),1]
for (i in 2:(ncol(dist_matr) - 1)) {
	j = j + 1
	distvec <- append(distvec, dist_matr[j:nrow(dist_matr),i])
}
# do clustering
cluster <- agnes(distvec, diss = TRUE, method = "average")

# plot dendrogram
plot(cluster, which.plots = 2, hang = -1, label = rownames(dist_matr), main = "", axes = FALSE, xlab = "", ylab = "", sub = "")

# make heatmap showing pairwise sample distances - in same order as cluster result!
heatplot(dist_matr[cluster$order,cluster$order], dend = c("none"),  cols.default = FALSE, lowcol = "black", highcol = "white", scale="none", margins = c(7,7))


#### Principal Coordinates Analysis (PCoA) of samples ####

library(made4)

# give vector of indices/samples to include

#these <- c(1:length(sample)) # in this case all samples

#these <- c(g_summer_tr_west_surface, g_winter_tr_west_surface) # in this case all samples

these <- g_shared_stations
  
#these <- g_winter


these <- intersect(these, which(!is.na(Depth)))
these <- intersect(these, which(Dept <= 1))
these <- intersect(these, which(!is.na(Sal)))
these <- these[ sort(Depth[these], index.return = TRUE, decreasing = TRUE)$ix ]

pco1 <- dudi.pco(lingoes(as.dist(spearman_matr[these, these])), scannf=FALSE, nf=3)
plot(pco1$eig, xlim = c(1,20))

ix <- (Sal[these] - min(Sal[these], na.rm = TRUE))*100 + 1
cols <- rainbow(max(ix, na.rm = TRUE) + 1, s = 1, v = 1, start = 0, end = 0.86, alpha = 1)
cols <- cols[length(cols):1]

cols2 <- c(1:length(sample))
cols2[g_summer] <- "red"
cols2[g_winter] <- "blue"

pitch <- c(1:length(sample))
pitch[g_summer] <- 20
pitch[g_winter] <- 17


plot(pco1$li[,1],  pco1$li[,2], cex = Depth[these]/10, col = cols2[these], pch = 20, xlab = "PC1", ylab = "PC2" )
plot(pco1$li[,2],  pco1$li[,3], cex = Depth[these]/10, col = cols2[these], pch = 20, xlab = "PC2", ylab = "PC3")

plot(pco1$li[,1],  pco1$li[,2], cex = Depth[these]/2, col = cols[these], pch = pitch[these], xlab = "PC1", ylab = "PC2" )
plot(pco1$li[,2],  pco1$li[,3], cex = Depth[these]/2, col = cols[these], pch = pitch[these], xlab = "PC2", ylab = "PC3")



#plot(pco1$li[,1],  pco1$li[,2], cex = Depth[these]/30, col = cols[ix])

plot(pco1$li[,1],  pco1$li[,2], col = "white", xlab = "PC1", ylab = "PC2", ylim = c(-0.3,0.45))
for (i in 1:length(ix)) {
	if (!is.na(ix[i])) {
		points(pco1$li[i,1],  pco1$li[i,2], cex = 2 + Depth[these[i]]/30, col = cols[ix[i]], pch = 20)
		points(pco1$li[i,1],  pco1$li[i,2], cex = 1.5 + Depth[these[i]]/45, col = "black")
	}
}

# color scale
plot(length(cols):1, 1:length(cols) - 1:length(cols), col = cols, pch = "|")

# plotting pc1 vs Sal
plot(pco1$li[,1], Sal[these], col = "white", xlab = "PC1", ylab = "Salinity")
for (i in 1:length(ix)) {
	if (!is.na(ix[i])) {
		points(pco1$li[i,1], Sal[these[i]], cex = 2 + Depth[these[i]]/30, col = cols[ix[i]], pch = 20)
		points(pco1$li[i,1], Sal[these[i]], cex = 1.5 + Depth[these[i]]/45, col = "black")
	}
}

# plotting pc2 vs Depth
plot(pco1$li[,2], Depth[these], col = "white", xlab = "PC2", ylab = "Depth")
for (i in 1:length(ix)) {
	if (!is.na(ix[i])) {
		points(pco1$li[i,2], Depth[these[i]], cex = 2 + Depth[these[i]]/30, col = cols[ix[i]], pch = 20)
		points(pco1$li[i,2], Depth[these[i]], cex = 1.5 + Depth[these[i]]/45, col = "black")
	}
}


#### correlate the first three PC:s against env parameters #### 

matr <- matrix(nrow = nrow(env2), ncol = 3)
for (i in 1:nrow(env2)) {
	matr[i,1] <- cor.test(env2[i, these], pco1$li[,1], method = "spearman")$est
	matr[i,2] <- cor.test(env2[i,these], pco1$li[,2], method = "spearman")$est
	matr[i,3] <- cor.test(env2[i,these], pco1$li[,3], method = "spearman")$est
}
cbind(rownames(env2), round(matr, 2))

# winter only output

     [,1]    [,2]    [,3]    [,4]   
[1,] "Depth" "0.18"  "-0.63" "-0.09"
[2,] "Sal"   "0.9"   "0.05"  "0.39" 
[3,] "Lat"   "-0.34" "-0.51" "-0.62"
[4,] "Lon"   "-0.67" "-0.47" "-0.39"

# all samples (> 500 reads)
     [,1]        [,2]    [,3]    [,4]   
[1,] "Depth"     "0.09"  "-0.73" "0.02" 
[2,] "Sal"       "0.88"  "-0.31" "0.11" 
[3,] "Lat"       "-0.48" "-0.16" "-0.23"
[4,] "Lon"       "-0.7"  "-0.17" "-0.14"
[5,] "Is_summer" "0.08"  "0.28"  "-0.62"


############# phylogentic - ecological linking #######

tree<-read.newick(treefile)
tree$tip.label<-paste(sapply(strsplit(as.character(tree$tip.label),"_"),"[[",1),sapply(strsplit(as.character(tree$tip.label),"_"),"[[",2),sep="_")

to.remove<-which((tree$tip.label %in% id)==FALSE) # substract the sequences from ARB
tree.reduced<-drop.tip(tree, to.remove)

all(tree.reduced$tip.label %in% id)

## Plot the tree
#pdf(file="Tree.pdf")
#plot(tree.reduced,show.tip.label=F)
#add.scale.bar(length=2)
#dev.off()

# 2. Compute cophenetic distance
coph.dist<-cophenetic(tree.reduced)
diag(coph.dist)<-NA
#coph.dist[coph.dist>3]<-NA # This removes cophenetic distances bigger than 3 - original!
coph.dist[coph.dist>1.5]<-NA # This removes cophenetic distances bigger than 1.5

phylo_dist_matr = matrix(ncol = length(id), nrow = length(id))
ix = match(tree.reduced$tip.label, id)
phylo_dist_matr[ix,ix] = coph.dist

these = 1:length(sample)
#these = g_surface
#these = g_joint

# calculating salinity niche value

salinity_niche_value = rep(NA, length(id))
for (i in 1:length(id)) {
  if (sum(norm_reads[i,these]) == 0) {
    salinity_niche_value[i] = NA 
  } else {
    salinity_niche_value[i] = sum(Sal[these]*norm_reads[i,these])/sum(norm_reads[i,these])
  }
}
salinity_niche_diff_matr = as.matrix(dist(as.matrix(salinity_niche_value, ncol = 1), method = "manhattan"))

season_niche_value = rep(NA, length(id))
for (i in 1:length(id)) {
  if (sum(norm_reads[i,these]) == 0) {
    season_niche_value[i] = NA 
  } else {
    season_niche_value[i] = sum(Season[these]*norm_reads[i,these])/sum(norm_reads[i,these])
  }
}
season_niche_diff_matr = as.matrix(dist(as.matrix(season_niche_value, ncol = 1), method = "manhattan"))

temperature_niche_value = rep(NA, length(id))
for (i in 1:length(id)) {
  if (sum(norm_reads[i,these]) == 0) {
    temperature_niche_value[i] = NA 
  } else {
    temperature_niche_value[i] = sum(Temp[these]*norm_reads[i,these])/sum(norm_reads[i,these])
  }
}
temperature_niche_diff_matr = as.matrix(dist(as.matrix(temperature_niche_value, ncol = 1), method = "manhattan"))

spearman_niche_diff_matr = matrix(ncol = length(id), nrow = length(id))
ok = which(apply(norm_reads[,these], 1, sum) > 0)
temp = cor(t(norm_reads[ok,these]), method = "spearman")
spearman_niche_diff_matr[ok, ok] = (-1*temp + 1) / 2

ok = which(apply(binary_reads[,these], 1, sum) >= 1) # 1
as_dist_phylo_dist_matr = as.dist(phylo_dist_matr[ok,ok])
as_dist_salinity_niche_diff_matr = as.dist(salinity_niche_diff_matr[ok,ok])
as_dist_season_niche_diff_matr = as.dist(season_niche_diff_matr[ok,ok])
as_dist_spearman_niche_diff_matr = as.dist(spearman_niche_diff_matr[ok,ok])
as_dist_temperature_niche_diff_matr = as.dist(temperature_niche_diff_matr[ok,ok])

ok = intersect(which(!is.na(as_dist_phylo_dist_matr)),  which(!is.na(as_dist_salinity_niche_diff_matr)))
as_dist_phylo_dist_matr = as_dist_phylo_dist_matr[ok]
as_dist_salinity_niche_diff_matr = as_dist_salinity_niche_diff_matr[ok]
as_dist_season_niche_diff_matr = as_dist_season_niche_diff_matr[ok]
as_dist_spearman_niche_diff_matr = as_dist_spearman_niche_diff_matr[ok]
as_dist_temperature_niche_diff_matr = as_dist_temperature_niche_diff_matr[ok]

len = c()
sal_diff = c()
seas_diff = c()
spear_diff = c()
temp_diff = c()
phyl_dist = c()
j = -0.01
k = 0
for (i in 1:300) {
  j = j + 0.01
  k = k + 0.01
  ix = intersect(which(as_dist_phylo_dist_matr >= j), which(as_dist_phylo_dist_matr < k))
  len[i] = length(ix)
  sal_diff[i] = mean(as_dist_salinity_niche_diff_matr[ix], na.rm = TRUE)
  seas_diff[i] = mean(as_dist_season_niche_diff_matr[ix], na.rm = TRUE)
  spear_diff[i] = mean(as_dist_spearman_niche_diff_matr[ix], na.rm = TRUE)
  temp_diff[i] = mean(as_dist_temperature_niche_diff_matr[ix], na.rm = TRUE)
  phyl_dist[i] = j
}
par(mfcol = c(2,2))
plot(phyl_dist[1:300], sal_diff[1:300], xlab = "Phylogenetic distance", ylab = "Salinity niche difference")
plot(phyl_dist[1:300], seas_diff[1:300], xlab = "Phylogenetic distance", ylab = "Season niche difference")
plot(phyl_dist[1:300], temp_diff[1:300], xlab = "Phylogenetic distance", ylab = "Temperature niche difference")
plot(phyl_dist[1:300], spear_diff[1:300], xlab = "Phylogenetic distance", ylab = "Spearman niche difference")


# Organize the taxonomy
a<-strsplit(taxonomy,";")
library(stringi)
res<-as.data.frame(t(stri_list2matrix(a)))
colnames(res)<-c("Domain","Phylum","Class","Order","Family","Genus")

maxdist = 1.5
layout(matrix(c(1,1,1,1,2,3,4,5,6,7,8), 11, 1, byrow = TRUE))
par(mar=c(4,10,4,4))
plot(phyl_dist, sal_diff, type="l",cex=0.6, xlab="Between-OTU Phylogenetic Distance", ylab="Between-OTU Niche Difference", pch=19, xlim=c(0,maxdist), ylim=c(3,12))
points(phyl_dist, sal_diff, cex=0.6, pch=19)
points(phyl_dist, 20*seas_diff, type="l", cex=0.4, lty=2, col = "blue")
points(phyl_dist, 20*seas_diff, cex=0.6, pch=3, col = "blue")
#points(phyl_dist, 1.5*temp_diff, type="l", cex=0.4, lty=2, col = "blue")
#points(phyl_dist, 1.5*temp_diff, cex=0.6, pch=3, col = "blue")
abline(v=seq(0,7,by=0.1),lty=2,col="gray")
legend("bottomright",c("Salinity","Season"),pch=c(19,3),inset=0.05,lty=c(1,2),cex=1,bg="white", col=c("black", "blue"))
#abline(h=mean(mitjana.sal,na.rm=T),lty=2,col="gray")
xlab = rep("", ncol(res))
xlab[1] = "Between-OTU Phylogenetic Distance"
par(mar=c(2,10,1,4),cex.axis=0.7,las=1)
for (i in ncol(res):1) {
  dist = c()
  for (j in 1:nlevels(res[,i])) {
      if (levels(res[,i])[j]!="Unclassified") {
        if (levels(res[,i])[j]!="unclassified") {
          if (levels(res[,i])[j]!="Uncultured") {
            if (levels(res[,i])[j]!="uncultured") {
              ix = which(levels(res[,i])[j]==res[,i])
              dist = c(dist, as.dist(phylo_dist_matr[ix,ix]))
            }
          }
        }
      }
  }
  hist(dist, nclass=200, xlim = c(0,maxdist), main = NA, col="black", xlab = xlab[i])
  legend("right",colnames(res)[i], inset=0.05, bty = "n", cex = 1)
}



x1 = which(as_dist_phylo_dist_matr < 0.1)
x2 = intersect(which(as_dist_phylo_dist_matr >= 0.1), which(as_dist_phylo_dist_matr < 0.2))
x3 = intersect(which(as_dist_phylo_dist_matr >= 0.2), which(as_dist_phylo_dist_matr < 0.3))
x4 = intersect(which(as_dist_phylo_dist_matr >= 0.3), which(as_dist_phylo_dist_matr < 0.5))
x5 = intersect(which(as_dist_phylo_dist_matr >= 0.5), which(as_dist_phylo_dist_matr < 1))
x6 = intersect(which(as_dist_phylo_dist_matr >= 1), which(as_dist_phylo_dist_matr < 2))
x7 = intersect(which(as_dist_phylo_dist_matr >= 2), which(as_dist_phylo_dist_matr < 3))

#boxplot(as_dist_spearman_niche_diff_matr[x1], as_dist_spearman_niche_diff_matr[x2], as_dist_spearman_niche_diff_matr[x3], as_dist_spearman_niche_diff_matr[x4], as_dist_spearman_niche_diff_matr[x5], as_dist_spearman_niche_diff_matr[x6], as_dist_spearman_niche_diff_matr[x7])
#boxplot(as_dist_salinity_niche_diff_matr[x1], as_dist_salinity_niche_diff_matr[x2], as_dist_salinity_niche_diff_matr[x3], as_dist_salinity_niche_diff_matr[x4], as_dist_salinity_niche_diff_matr[x5], as_dist_salinity_niche_diff_matr[x6], as_dist_salinity_niche_diff_matr[x7])
boxplot(as_dist_season_niche_diff_matr[x1], as_dist_season_niche_diff_matr[x2], as_dist_season_niche_diff_matr[x3], as_dist_season_niche_diff_matr[x4], as_dist_season_niche_diff_matr[x5], as_dist_season_niche_diff_matr[x6], as_dist_season_niche_diff_matr[x7])


############# Calc pairwise OTU dists ##################

# Most abundant OTUs:

#these <- c(1:length(sample))
#these <- g_summer
#these <- g_winter
#these <- intersect(g_surface, which(Sal < 20))
these <- intersect(g_summer, which(!is.na(Sal)))
#these <- intersect(g_summer, intersect(g_surface, which(Sal < 20)))
#these <- intersect(g_winter, intersect(g_surface, which(Sal < 20)))

top_otus <- sort(apply(norm_reads[,these], 1, mean), decreasing = TRUE, index.return = TRUE)$ix[1:100] # top 100 in this case!
top_avs <- sort(apply(norm_reads[,these], 1, mean), decreasing = TRUE)[1:100] # top 100 in this case!

top_norm_reads <- norm_reads[top_otus,]

# calc cors:

spearman_otu_matr_est <- matrix(ncol = nrow(top_norm_reads), nrow = nrow(top_norm_reads))
spearman_otu_matr_pval <- spearman_otu_matr_est
for (i in 1:nrow(top_norm_reads)) {
	for (j in 1:nrow(top_norm_reads)) {
		#ok <- which(top_norm_reads[i,these] + top_norm_reads[j,these] > 0) # for skipping double zeros
		ok <- which(top_norm_reads[i,these] + top_norm_reads[j,these] > -1) # for using all
		spearman_otu_matr_est[i,j] = cor.test(top_norm_reads[i,these[ok]], top_norm_reads[j,these[ok]], method = "spearman")$est
		spearman_otu_matr_pval[i,j] = cor.test(top_norm_reads[i,these[ok]], top_norm_reads[j,these[ok]], method = "spearman")$p.val
	}
}
#spearman_otu_matr_est <- (-1*spearman_otu_matr_est + 1) / 2
spearman_dist_otu_matr_est <- (-1*spearman_otu_matr_est + 1) / 2

taxonomy[top_otus][1:10]
temp1 <- sort(spearman_otu_matr_est[1,], decreasing = TRUE)[1:10]
temp2 <- id[top_otus[sort(spearman_otu_matr_est[1,], decreasing = TRUE, index.return=TRUE)$ix]][1:10]
temp3 <- taxonomy[top_otus[sort(spearman_otu_matr_est[1,], decreasing = TRUE, index.return=TRUE)$ix]][1:10]
cbind(round(temp1, 2), temp2, temp3)

ix <- (Sal[these] - min(Sal[these], na.rm = TRUE))*100 + 1
cols <- rainbow(max(ix, na.rm = TRUE) + 1, s = 1, v = 1, start = 0, end = 0.86, gamma = 1, alpha = 1)
cols <- cols[length(cols):1]

temp1 <- top_otus[sort(spearman_otu_matr_est[1,], decreasing = TRUE, index.return=TRUE)$ix][1]
temp2 <- top_otus[sort(spearman_otu_matr_est[1,], decreasing = TRUE, index.return=TRUE)$ix][2]

#log plot - 0s will dissapear
#plot(log10(norm_reads[temp1,these]), log10(norm_reads[temp2,these]), cex = log10(Depth[these]*10), pch = 20, col = cols[ix], xlab = "Spartobacterium_OTU", ylab = "GpIIa_OTU", xlim = c(-4,0), ylim=c(-4,0))

# plot where 0s will be given a value 10^-4
temp1 <- norm_reads[temp1,these]
temp1[which(temp1 == 0)] <- 10^-4
temp2 <- norm_reads[temp2,these]
temp2[which(temp2 == 0)] <- 10^-4 
plot(log10(temp1), log10(temp2), cex = log10(Depth[these]*10), pch = 20, col = cols[ix], xlab = "Spartobacterium_OTU", ylab = "GpIIa_OTU", xlim = c(-4,0), ylim=c(-4,0), axes = FALSE)
axis(1, labels = c("0", "0.001", "0.01", "0.1", "1"), at = c(-4, -3,-2,-1,0))
axis(2, labels = c("0", "0.001", "0.01", "0.1", "1"), at = c(-4, -3,-2,-1,0))

# Depth scale
plot(c(1, 2, 3), c(1, 1, 1), cex = log10(c(1, 10, 100)*10), axes = FALSE, xlim = c(1,10), ylim = c(1,5), xlab="", ylab="")
axis (1, labels = c("1", "10", "100"), at = c(1, 2, 3))

# Salinity scale
temp <- seq(from = min(Sal[these]), to = max(Sal[these]), by = 0.01) 
plot(temp, rep(1, length(temp)), col = cols[(temp - min(Sal[these]))*100 + 1], pch = "|", xlim = c(0,35), ylim = c(1,5), axes = FALSE, xlab="", ylab="")
axis(1)




# NMDS

library(vegan)

mds <- metaMDS(spearman_dist_otu_matr_est)


cols <- c(1:length(top_otus))
cols[] <- "black"
cols[grep("Cyanobacteria", taxonomy[top_otus])] <- "lightseagreen"
cols[grep("Bacteroidetes", taxonomy[top_otus])] <- "lightskyblue1"
cols[grep("Actinobacteria", taxonomy[top_otus])] <- "lightpink1" 
cols[grep("Planctomycetes", taxonomy[top_otus])] <- "orchid1"
cols[grep("Chloroflexi", taxonomy[top_otus])] <- "lightslateblue"
cols[grep("Verrucomicrobia", taxonomy[top_otus])] <- "orange"
cols[grep("Alphaproteobacteria", taxonomy[top_otus])] <- "lightblue3"
cols[grep("Betaproteobacteria", taxonomy[top_otus])] <- "lightcoral"
cols[grep("Gammaproteobacteria", taxonomy[top_otus])] <- "lightgoldenrod2"
cols[grep("Epsilonproteobacteria", taxonomy[top_otus])] <- "lightgreen"


plot(mds$points[,1], mds$points[,2], cex = log10(top_avs*100000), col = cols, pch = 19)

# Make input to Medusa

cols <- c(1:length(top_otus))
cols[] <- "c 0,0,0"
cols[grep("Cyanobacteria/Chloroplast;Chloroplast", taxonomy[top_otus])] <-  "c 144,238,144" # "lightgreen"
cols[grep("Cyanobacteria/Chloroplast;Cyanobacteria", taxonomy[top_otus])] <- "c 32,178,170" # "lightseagreen"
cols[grep("Bacteroidetes", taxonomy[top_otus])] <- "c 176,226,255" # "lightskyblue1" 
cols[grep("Actinobacteria", taxonomy[top_otus])] <- "c 255,174,185" # "lightpink1"
cols[grep("Planctomycetes", taxonomy[top_otus])] <- "c 255,131,250" # "orchid1"
cols[grep("Chloroflexi", taxonomy[top_otus])] <- "c 132,112,255" # "lightslateblue"
cols[grep("Verrucomicrobia", taxonomy[top_otus])] <- "c 255,165,0" # "orange" 
cols[grep("Alphaproteobacteria", taxonomy[top_otus])] <- "c 154,192,205" # "lightblue3"
cols[grep("Betaproteobacteria", taxonomy[top_otus])] <- "c 240,128,128" # "lightcoral"
cols[grep("Gammaproteobacteria", taxonomy[top_otus])] <- "c 238,220,130" # "lightgoldenrod2"
cols[grep("Epsilonproteobacteria", taxonomy[top_otus])] <- "c 255,192,203" # "pink"

cat(c("*edges", "\n"), file = "medusa_input.txt")
for (i in 1:(length(top_otus) - 1)) {
	for (j in (i + 1):length(top_otus)) {
		cat(c(i,j, "i 3", paste("c", round(1 - spearman_dist_otu_matr_est[i,j], 2), sep = " "), "\n"),  sep = "\t", append = TRUE, file = "medusa_input.txt")
  	}
}
cat(c("*nodes", "\n"), append = TRUE, file = "medusa_input.txt")
for (i in 1:length(top_otus)) {
	cat(c(i,i,i,cols[i], "s 0", "\n"),  sep = "\t", append = TRUE, file = "medusa_input.txt")
}


### corr between coomunity differnce with env difference ###

dist_matr = spearman_matr

temp <- c(1)
for (k in 1:nrow(env)) { 
#for (k in 5:5) {     
  diff_matr <- matrix(ncol = ncol(reads), nrow = ncol(reads))
  for (i in 1:ncol(env)) {
    for (j in 1:ncol(env)) {
      diff_matr[i,j] = abs(env[k,i] - env[k,j])
    }
  }
  temp[k] <- cor.test(as.vector(diff_matr), as.vector(dist_matr), metod = "spearman")$est
  #temp[k] <- cor.test(diff_matr, as.matrix(bray), metod = "spearman")$est
}
cbind(rownames(env), temp)



####################################################################################################################
####################################################################################################################

The following has not be updated and will likely have to be recoded to fit with data!!


################
#### BioEnv ####

library(vegan)

reads_flipped <- matrix(nrow = ncol(reads), ncol = nrow(reads))
for (i in 1:ncol(reads)) {
	reads_flipped[i,] <- reads[,i]
}

env_flipped  <- matrix(nrow = ncol(env2), ncol = nrow(env2))
for (i in 1:ncol(env2)) {
	env_flipped[i,] <- env2[,i]
}
colnames(env_flipped) <- rownames(env2) 
rownames(env_flipped) <- colnames(env2) 
colnames(reads_flipped) <- rownames(reads) 
rownames(reads_flipped) <- colnames(reads) 

these <- S
#these <- all
Y <- as.data.frame(env_flipped[these,])
Y <- Y[,4:12]
ok <- which(!is.na(apply(Y, 1, sum)))

these <- these[ok]
Y <- as.data.frame(env_flipped[these,])
X <- as.data.frame(reads_flipped[these,])
Y <- Y[c(4,5,6,7,8,9,10,11,12)]

bioenv(X, Y, method = "spearman", index = "bray", upto = ncol(Y), trace = FALSE, partial = NULL)
#bioenv(X, Y, method = "spearman", index = "bray", upto = 3, trace = FALSE, partial = NULL)

matr <- matrix(ncol = 4, nrow = ncol(Y))
#for (k in 1:ncol(Y)) {
for (k in 2:2) {
	apa <- uf_matr[these,these]
	apa[] <- NA
	for (i in 1:nrow(Y)) {
		for (j in 1:nrow(Y)) {
			apa[i,j] <- abs(Y[i,k] - Y[j,k])
		}
	}
	matr[k,1] <- round( cor.test(apa, uf_matr[these,these], method = "spearman")$est, 2)
	matr[k,2] <- round( cor.test(apa, spearman_matr[these,these], method = "spearman")$est, 2)
	matr[k,3] <- round( cor.test(apa, bray_matr[these,these], method = "spearman")$est, 2) 
	matr[k,4] <- round( cor.test(apa, geo_matr[these,these], method = "spearman")$est, 2) 

	#matr[k,1] <- round( cor.test(apa, uf_matr[these,these])$est, 2)
	#matr[k,2] <- round( cor.test(apa, spearman_matr[these,these])$est, 2)
	#matr[k,3] <- round( cor.test(apa, bray_matr[these,these])$est, 2) 
	#matr[k,4] <- round( cor.test(apa, geo_matr[these,these])$est, 2) 

}
matr <- cbind(colnames(Y), matr)
matr <- rbind(c("..", "UF", "Spear", "Bray", "Geo"), matr)
matr

#all
      [,1]   [,2]    [,3]    [,4]   [,5]   
 [1,] ".."   "UF"    "Spear" "Bray" "Geo"  
 [2,] "Temp" "0.22"  "0.33"  "0.34" "0.22" 
 [3,] "Sal"  "0.29"  "0.62"  "0.59" "0.4"  
 [4,] "Par"  "0.08"  "0.1"   "0.13" "0.11" 
 [5,] "NO23" "0.03"  "0.13"  "0.09" "0.14" 
 [6,] "NO2"  "-0.07" "0.04"  "0.02" "0.03" 
 [7,] "NO3"  "0.02"  "0.12"  "0.08" "0.16" 
 [8,] "PO4"  "0.48"  "0.48"  "0.48" "-0.02"
 [9,] "SI"   "0.48"  "0.56"  "0.56" "0.08" 
[10,] "O2"   "0.49"  "0.52"  "0.53" "0.04" 

#S
      [,1]   [,2]   [,3]    [,4]   [,5]  
 [1,] ".."   "UF"   "Spear" "Bray" "Geo" 
 [2,] "Temp" "0.24" "0.51"  "0.51" "0.44"
 [3,] "Sal"  "0.47" "0.81"  "0.8"  "0.53"
 [4,] "Par"  "0.01" "0.03"  "0.01" "0.07"
 [5,] "NO23" "0.11" "0.27"  "0.27" "0.18"
 [6,] "NO2"  "0.14" "0.33"  "0.33" "0.34"
 [7,] "NO3"  "0.13" "0.31"  "0.3"  "0.21"
 [8,] "PO4"  "0.05" "0.01"  "0.01" "0.06"
 [9,] "SI"   "0.36" "0.55"  "0.54" "0.37"
[10,] "O2"   "0.42" "0.72"  "0.71" "0.56"

plot(apa, spearman_matr[these,these], xlab = "Difference in salinity", ylab = "Difference in community")
plot(geo_matr[these,these], spearman_matr[these,these], xlab = "Geographic distance (km)", ylab = "Difference in community")



####################################
#### Making clade count tables ####

### Phylum level ###
### Count seqs in clades ###
level = 3
clades <- levels(factor(taxonomy))
for (i in 1:length(clades)) {
	if (length( matrix(unlist(strsplit(clades[i],";")), 1)[1,] ) >= level) {
		string <- matrix(unlist(strsplit(clades[i],";")), 1)[1,1]
		for (j in 2:level) {
			string <- paste(string, matrix(unlist(strsplit(clades[i],";")), 1)[1,j], sep = ";")
		}
		clades[i] <- string
	} else {
		clades[i] <- NA
	}
}
clades <- levels(factor(clades))
#clades <- clades[ setdiff(c(1:length(clades)), grep("unclassified_", clades)) ]
clades <- clades[ setdiff(c(1:length(clades)), grep("no_match", clades)) ]
clades[length(clades) + 1] <- "others"
clade_reads <- matrix(nrow = length(clades), ncol = ncol(reads))
colnames(clade_reads) <- colnames(reads)
all_these <- vector(length = 0) 
for (i in 1:length(clades)) {
	these <- grep (clades[i], taxonomy)
	all_these <- union(these, all_these)
	for (j in 1:ncol(clade_reads)) {
		clade_reads[i,j] <- sum(reads[these,j])
	}
}
others <- setdiff(c(1:length(taxonomy)), all_these)
for (j in 1:ncol(clade_reads)) {
	clade_reads[length(clades),j] <- sum(reads[others,j])
}
norm_clade_reads <- clade_reads
for (i in 1:ncol(clade_reads)) {
	norm_clade_reads[,i] <- clade_reads[,i]/sum(clade_reads[,i])
}
phylum_reads <- clade_reads
norm_phylum_reads <- norm_clade_reads
phylum <- clades


### Phylum / Class level ###
### Count seqs in clades ###

level = 4
clades <- levels(factor(taxonomy))
for (i in 1:length(clades)) {
	if (length( matrix(unlist(strsplit(clades[i],";")), 1)[1,] ) >= level) {
		string <- matrix(unlist(strsplit(clades[i],";")), 1)[1,1]
		for (j in 2:level) {
			string <- paste(string, matrix(unlist(strsplit(clades[i],";")), 1)[1,j], sep = ";")
		}
		if (length( grep("Proteobacteria", string) ) > 0) {
			clades[i] <- string
		} else {
			clades[i] <- NA
		}
	} else {
		clades[i] <- NA 
	}
}
proteo_clades <- levels(factor(clades))

level = 3
clades <- levels(factor(taxonomy))
for (i in 1:length(clades)) {
	if (length( matrix(unlist(strsplit(clades[i],";")), 1)[1,] ) >= level) {
		string <- matrix(unlist(strsplit(clades[i],";")), 1)[1,1]
		for (j in 2:level) {
			string <- paste(string, matrix(unlist(strsplit(clades[i],";")), 1)[1,j], sep = ";")
		}
		if (length( grep("Proteobacteria", string) ) == 0) {
			clades[i] <- string
		} else {
			clades[i] <- NA
		}
	} else {
		clades[i] <- NA
	}
}
clades <- levels(factor(clades))
clades <- c(clades, proteo_clades)
#clades <- clades[ setdiff(c(1:length(clades)), grep("unclassified_", clades)) ]
clades <- clades[ setdiff(c(1:length(clades)), grep("no_match", clades)) ]
clades[length(clades) + 1] <- "others"
clade_reads <- matrix(nrow = length(clades), ncol = ncol(reads))
colnames(clade_reads) <- colnames(reads)
all_these <- vector(length = 0) 
for (i in 1:length(clades)) {
	these <- grep (clades[i], taxonomy)
	all_these <- union(these, all_these)
	for (j in 1:ncol(clade_reads)) {
		clade_reads[i,j] <- sum(reads[these,j])
	}
}
others <- setdiff(c(1:length(taxonomy)), all_these)
for (j in 1:ncol(clade_reads)) {
	clade_reads[length(clades),j] <- sum(reads[others,j])
}
norm_clade_reads <- clade_reads
rownames(norm_clade_reads) <- clades
for (i in 1:ncol(clade_reads)) {
	norm_clade_reads[,i] <- clade_reads[,i]/sum(clade_reads[,i])
}
phylumclass_reads <- clade_reads
norm_phylumclass_reads <- norm_clade_reads
phylumclass <- clades

### Class level ###
### Count seqs in clades ###

level = 4
clades <- levels(factor(taxonomy))
for (i in 1:length(clades)) {
	if (length( matrix(unlist(strsplit(clades[i],";")), 1)[1,] ) >= level) {
		string <- matrix(unlist(strsplit(clades[i],";")), 1)[1,1]
		for (j in 2:level) {
			string <- paste(string, matrix(unlist(strsplit(clades[i],";")), 1)[1,j], sep = ";")
		}
		clades[i] <- string
	} else {
		clades[i] <- NA
	}
}
clades <- levels(factor(clades))
#clades <- clades[ setdiff(c(1:length(clades)), grep("unclassified_", clades)) ]
clades <- clades[ setdiff(c(1:length(clades)), grep("no_match", clades)) ]
clades[length(clades) + 1] <- "others"
clade_reads <- matrix(nrow = length(clades), ncol = ncol(reads))
colnames(clade_reads) <- colnames(reads)
all_these <- vector(length = 0) 
for (i in 1:length(clades)) {
	these <- grep (clades[i], taxonomy)
	all_these <- union(these, all_these)
	for (j in 1:ncol(clade_reads)) {
		clade_reads[i,j] <- sum(reads[these,j])
	}
}
others <- setdiff(c(1:length(taxonomy)), all_these)
for (j in 1:ncol(clade_reads)) {
	clade_reads[length(clades),j] <- sum(reads[others,j])
}
norm_clade_reads <- clade_reads
for (i in 1:ncol(clade_reads)) {
	norm_clade_reads[,i] <- clade_reads[,i]/sum(clade_reads[,i])
}
class_reads <- clade_reads
norm_class_reads <- norm_clade_reads
class <- clades

### Genus level ###

### Count seqs in clades ###
clades <- levels(factor(taxonomy))
#clades <- clades[ setdiff(c(1:length(clades)), grep("unclassified_", clades)) ]
clades <- clades[ setdiff(c(1:length(clades)), grep("no_match", clades)) ]
clades <- clades[grep("\\.", clades)]
clades[length(clades) + 1] <- "others"
clade_reads <- matrix(nrow = length(clades), ncol = ncol(reads))
colnames(clade_reads) <- colnames(reads)
all_these <- vector(length = 0)
for (i in 1:length(clades)) {
	these <- grep (clades[i], taxonomy)
	all_these <- union(these, all_these)
	for (j in 1:ncol(clade_reads)) {
		clade_reads[i,j] <- sum(reads[these,j])
	}
}
others <- setdiff(c(1:length(taxonomy)), all_these)
for (j in 1:ncol(clade_reads)) {
	clade_reads[length(clades),j] <- sum(reads[others,j])
}
norm_clade_reads <- clade_reads
for (i in 1:ncol(clade_reads)) {
	norm_clade_reads[,i] <- clade_reads[,i]/sum(clade_reads[,i])
}
genus_reads <- clade_reads
norm_genus_reads <- norm_clade_reads
genus <- clades

